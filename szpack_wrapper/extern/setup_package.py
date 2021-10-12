# Licensed under a 3-clause BSD style license - see LICENSE.rst

from collections import defaultdict

from distutils.core import Extension

import subprocess
import numpy

from extension_helpers import get_compiler
from extension_helpers import add_openmp_flags_if_available
from pathlib import Path


szpack_dir = Path(__file__).parent.joinpath('SZpack.v1.1.1')


def get_gslconfig_cmd():
    """Get the gsl-config executable."""
    cmd = 'gsl-config'
    try:
        subprocess.check_output(
                (cmd, '--version'),
                stderr=subprocess.STDOUT
                ).decode().split('\n')[0].strip()
    except Exception as e:
        raise RuntimeError(f"error finding gsl-config: {e}")
    return cmd


def get_gsl_info():
    cmd = get_gslconfig_cmd()
    prefix, libs = subprocess.check_output(
            [cmd, '--prefix', '--libs']).decode().strip().split('\n')

    incdir = Path(prefix).joinpath('include')
    libdir = Path(prefix).joinpath('lib')
    libs = [lib[2:] for lib in libs.split() if lib.startswith('-l')]
    return {
            'incdir': incdir.as_posix(),
            'libdir': libdir.as_posix(),
            'libs': libs
            }


def get_extensions():

    cfg = defaultdict(list)

    szpack_files = [  # List of wcslib files to compile
        'Development/Simple_routines/Relativistic_MB.cpp',
        'Development/Simple_routines/nPl_derivatives.cpp',
        'Development/Simple_routines/routines.cpp',
        'Development/Integration/Patterson.cpp',
        'Development/Integration/Integration_routines.GSL.cpp',
        'Development/Integration/Chebyshev_Int.cpp',
        'src/SZ_Integral.5D.cpp',
        'src/SZ_Integral.3D.cpp',
        'src/SZ_asymptotic.cpp',
        'src/SZ_CNSN_basis.cpp',
        'src/SZ_CNSN_basis.opt.cpp',
        'SZpack.cpp',
        'python/SZpack.i',
        'python/SZpack.python.cpp'
        ]
    szpack_incdirs = [
            '',
            'include',
            'Development/Definitions',
            'Development/Integration',
            'Development/Simple_routines',
            'python'
            ]
    cfg['sources'].extend(
            szpack_dir.joinpath(x).as_posix() for x in szpack_files)
    cfg['include_dirs'].extend(
            szpack_dir.joinpath(x).as_posix() for x in szpack_incdirs)

    # external dependencies
    cfg['include_dirs'].append(numpy.get_include())
    cfg['libraries'].append('m')

    gsl_info = get_gsl_info()

    cfg['include_dirs'].append(gsl_info['incdir'])
    cfg['library_dirs'].append(gsl_info['libdir'])
    cfg['runtime_library_dirs'].append(gsl_info['libdir'])
    cfg['libraries'].extend(gsl_info['libs'])
    cfg['swig_opts'].extend(['-modern', '-c++'])

    if get_compiler() in ('unix', 'mingw32'):
        cfg['extra_compile_args'].extend([
            '-pedantic',
            '-Wno-newline-eof',
            '-Wno-unused-const-variable',
            ])

    extension = Extension('szpack_wrapper.extern._SZpack', **cfg)
    add_openmp_flags_if_available(extension)
    return [extension, ]
