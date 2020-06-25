#! /usr/bin/env python

from . import _SZpack


_excluded_from_all = set(globals().keys())

__version__ = 'v1.1.1'


# the below are copied from the SWIG generated SZpack.py file.
# TODO fix the args, add docs.


def compute_5d(*args):
    return _SZpack.compute_5d(*args)


def compute_3d(*args):
    return _SZpack.compute_3d(*args)


def compute_asym(*args):
    return _SZpack.compute_asym(*args)


def compute_CNSN(*args):
    return _SZpack.compute_CNSN(*args)


def compute_CNSN_opt(*args):
    return _SZpack.compute_CNSN_opt(*args)


def compute_combo(*args):
    return _SZpack.compute_combo(*args)


def compute_combo_means(*args):
    return _SZpack.compute_combo_means(*args)


def compute_combo_means_ex(*args):
    return _SZpack.compute_combo_means_ex(*args)


def compute_null(tau, TeSZ, betac_para, omega1, sigma, kappa, betac2_perp):
    return _SZpack.compute_null(
            tau, TeSZ, betac_para, omega1, sigma, kappa, betac2_perp)


__all__ = list(set(globals().keys()).difference(_excluded_from_all))
