A high-level wrapper for SZpack.
--------------------------------

.. image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
    :target: http://www.astropy.org
    :alt: Powered by Astropy Badge


This package provides some high-level functions to work with
`SZpack <http://www.jb.man.ac.uk/~jchluba/Science/SZpack/SZpack.html>`_
developed by J. Chluba and Eric R. Switzer.

SZpack License
--------------

The license section from the README file of the `SZpack.v1.1.1` tarball:

.. code:: text

    //==================================================================================================
    // LICENCE:
    //
    // This code and all contained libraries and subroutines can be used free of charge provided that:
    //
    // (i) their use will be acknowledged in publications
    //
    // (ii) the paper of
    //
    //	 	Chluba, Nagai, Sazonov, Nelson, MNRAS, 2012 (arXiv:1205.5778)
    //	 	Chluba, Switzer, Nagai, Nelson, 2012, arXiv:1211.3206
    //
    // 	will be cited, and the following papers are considered for citation:
    //		
    //		Sazonov & Sunyaev, ApJ, 1998
    //		Challinor & Lasenby, ApJ, 1998
    //		Itoh et al., ApJ, 1998
    //		Nozawa et al. ApJ, 1998 
    //      Nozawa et al. Nuovo Cimento B Series, 2006
    //
    // (iii) bugs will be immediately reported to Jens@Chluba.de
    //
    //==================================================================================================


Installation
------------

The SZpack depends on the
`GNU Scientific Library <https://www.gnu.org/software/gsl/>`_ (GSL), which has
to be installed and made available in the environment.

The low level python interface comes along with SZPack also depends on
`SWIG <http://www.swig.org/index.php>`_. Please refer to the documentation
for how to install.

To install ``szpack_wrapper``,

.. code:: text

    $ gsl-config --version  # check that GSL is installed
    2.6
    $ which swig  # check that swig is installed
    /usr/local/bin/swig
    $ pip install git+https://github.com/toltec-astro/szpack_wrapper

Behind the scene, the ``SZpack`` v1.1.1 is bundled with this package in the
``szpack_wrapper/extern`` folder, and an accompanying ``setup_package.py`` file
is used to leverage the
`extension-helpers <https://extension-helpers.readthedocs.io/en/latest/>`_
to build the code as a C extension.


SZpackWrapper License
---------------------

This project is Copyright (c) Zhiyuan Ma and licensed under
the terms of the BSD 3-Clause license. This package is based upon
the `Astropy package template <https://github.com/astropy/package-template>`_
which is licensed under the BSD 3-clause license. See the licenses folder for
more information.
