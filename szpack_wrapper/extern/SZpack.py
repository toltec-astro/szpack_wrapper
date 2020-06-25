#! /usr/bin/env python

import re
from pathlib import Path

__all__ = ['__version__', ]

_szpack_dir = list(Path(__file__).parent.glob('SZpack.v*'))[0]

__version__ = re.match(r'SZpack\.(v.+)', _szpack_dir.name).group(1)
