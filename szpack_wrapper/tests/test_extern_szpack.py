#! /usr/bin/env python


def test_extern_szpack():
    from ..extern import SZpack
    assert SZpack.__version__ == 'v1.1.1'
