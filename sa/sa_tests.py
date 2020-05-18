"""
sa_tests.py

Tests for Bluetooth BR/EDR secure (mutual) authentication procedure.

"""

from sa import *
log.setLevel(logging.DEBUG)


def test_sa():
    """Test secure authentication."""

    K   =  bytearray.fromhex('10f2e5d6c9a2630580a960856f66b029')
    C_S  = bytearray.fromhex('4579607928950b0bc5f422f00c64c38e')
    C_M  = bytearray.fromhex('a79060aa4f4638d907e261b4a5a3c612')
    BTADD_S  = bytearray.fromhex('404e36a8bf5f')
    BTADD_M  = bytearray.fromhex('20819A076931')
    SRES_S  = bytearray.fromhex('cca016d3')
    SRES_M  = bytearray.fromhex('8266e553')

    ComputedSRES_M, ComputedSRES_S = sa(K, C_M, C_S, BTADD_M, BTADD_S)

    assert ComputedSRES_M == SRES_M
    assert ComputedSRES_S == SRES_S


def test_sa2():
    """Test secure authentication."""

    K   =  bytearray.fromhex('06a789c1b0bdce23331370e2ebfcc26e')
    C_S  = bytearray.fromhex('f56a4415665e886654897febabefcb5d')
    C_M  = bytearray.fromhex('650b1addec9e276d5a7df677281de157')
    BTADD_S  = bytearray.fromhex('404e36a8bf5f')
    BTADD_M  = bytearray.fromhex('20819A076931')
    SRES_S  = bytearray.fromhex('d9c71d57')
    SRES_M  = bytearray.fromhex('3dac63b8')

    ComputedSRES_M, ComputedSRES_S = sa(K, C_M, C_S, BTADD_M, BTADD_S)

    # log.debug("ComputedSRES_M: {}".format(ba2hs(ComputedSRES_M)))
    # log.debug("        SRES_M: {}".format(ba2hs(SRES_M)))
    # log.debug("")
    # log.debug("ComputedSRES_S: {}".format(ba2hs(ComputedSRES_S)))
    # log.debug("        SRES_S: {}".format(ba2hs(SRES_S)))

    assert ComputedSRES_M == SRES_M
    assert ComputedSRES_S == SRES_S



if __name__ == "__main__":

    test_sa()
    test_sa2()
