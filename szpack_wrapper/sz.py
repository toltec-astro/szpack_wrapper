#! /usr/bin/env python

from astropy.cosmology import default_cosmology
from .extern import SZpack
from astropy import constants as const
import numpy as np
import astropy.units as u
from astropy import log


__all__ = ['SZ', ]


class SZ(object):
    """ This class defines high level interface to call SZpack.

    The SZpack works with the dimensionless (yet cosmology dependent)
    wavelength ``x`` defined as

    .. math::

        x \\equiv \\frac{h\\nu}{k_BT_{CMB0}}

    :meth:`wavelength_to_x` and :meth:`x_to_wavelength` can be used
    to convert between ``x`` and `~astropy.units.Quantity` instance.

    Parameters
    ----------
    cosmo : `~astropy.cosmology.Cosmology`

        The cosmology to use. `~astropy.cosmology.default_cosmology` is
        used if not set.
    """

    def __init__(self, cosmo=None):
        if cosmo is None:
            cosmo = default_cosmology.get()
        self._cosmo = cosmo

    @property
    def cosmo(self):
        return self._cosmo

    def wavelength_to_x(self, wavelength):
        """Return the dimensionless wavelength."""
        frequency = wavelength.to(u.GHz, equivalencies=u.spectral())
        x = (const.h * frequency) / (const.k_B * self.cosmo.Tcmb0)
        return x.to_value(u.dimensionless_unscaled)

    def x_to_wavelength(self, x):
        """Return the wavelength as `~astropy.units.Quantity`."""
        return (x * (const.k_B * self.cosmo.Tcmb0) / const.h).to(
                u.mm, u.spectral())

    def surface_brightness(
            self, runmode='3D',
            x=None,
            wavelength=None, **kwargs):
        """
        Compute the SZ surface_brightness.

        The input can be either given as the dimensionless ``x`` or
        as `~astropy.units.Quantity`.

        The output is the SZ surface brightness as `~astropy.units.Quantity`.

        The `runmode` and `kwargs` is passed to SZpack wrapper to execute
        the calculation.

        Refer to the README file of SZpack for more information of all
        run-modes supported and the associated arguments.

        Parameters
        ----------
        x : `~numpy.ndarray`

            Dimensionless Observer frame photon frequency (h nu / k T0)
        wavelength : `~astropy.units.Quantity`

            Observer frame photon wavelength/frequency.

        Returns
        -------
        `~astropy.units.Quantity`

            The SZ surface brightness.
        """
        _compute = getattr(self, f'_compute_{runmode}', None)
        if _compute is None:
            raise NotImplementedError(
                    f"compute run mode {runmode} is not implemented.")
        if sum([x is None, wavelength is None]) != 1:
            raise ValueError(
                    "specify observing frequency by one of "
                    "x, frequency, or wavelength.")
        # compute x
        if x is None:
            x = self.wavelength_to_x(wavelength)
        result = _compute(x, **kwargs)  # in Dn(x)
        # dndi value is from  SZpack.h line 73
        DnDI = 13.33914078 * self.cosmo.Tcmb0.to_value(u.K) ** 3
        return result * x ** 3 * DnDI * u.MJy / u.sr

    @staticmethod
    def _compute_3D(
            x, Dtau, Te_keV, betac, muc, betao, muo, eps_Int=1e-4,
            check_range=True
            ):
        if check_range:
            if np.min(x) < 0.1:
                raise ValueError(f"x < 0.1 at {np.argmin(x)}")
            if np.min(x) > 50.0:
                raise ValueError(f"x > 50. at {np.argmax(x)}")
        result = np.copy(x)
        log.debug(
                f'szpack.compute_3d(Dtau={Dtau}, Te_keV={Te_keV}, '
                f'betac={betac}, muc={muc}, betao={betao}, muo={muo})')
        SZpack.compute_3d(result, Dtau, Te_keV, betac, muc, betao, muo)
        return result

    @staticmethod
    def _compute_combo_means(
            x, tau, TeSZ_keV,
            betac_para, omega, sigma, kappa, betac_perp,
            check_range=True
            ):
        if check_range:
            if np.min(x) < 0.1:
                raise ValueError(f"x < 0.1 at {np.argmin(x)}")
            if np.min(x) > 50.0:
                raise ValueError(f"x > 50. at {np.argmax(x)}")
            if TeSZ_keV > 75.:
                raise ValueError(f'TeSZ_keV > 75.')
        result = np.copy(x).reshape((-1))
        log.debug(
                f'szpack.compute_combo_means(tau={tau}, TeSZ_keV={TeSZ_keV}, '
                f'betac_para={betac_para}, omega={omega}, '
                f'sigma={sigma}, kappa={kappa}, betac_perp={betac_perp})')
        SZpack.compute_combo_means(
                result, tau, TeSZ_keV,
                betac_para, omega, sigma, kappa, betac_perp)
        if np.isscalar(x):
            return result[0]
        return result.reshape(x.shape)
