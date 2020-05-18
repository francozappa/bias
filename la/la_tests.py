"""
la_tests.py

Tests for Bluetooth BR/EDR legacy (unilateral) authentication procedure.

"""

from la import *
log.setLevel(logging.INFO)


def test_la():
    """Test legacy authentication."""

    K   =  bytearray.fromhex('3b001a0f0830458bc17c40018b7fb197')

    C_V  = bytearray.fromhex('34fe03443bd6b70c7ff36bf3167702fa')
    BTADD_P  = bytearray.fromhex('38184c49f1fb')
    SRES  = bytearray.fromhex('7b28baf5')
    ComputedSRES = la(K, C_V, BTADD_P)
    log.debug("Challenge: {}, Response: {}".format(repr(C_V), repr(SRES)))
    assert ComputedSRES == SRES

    C_V  = bytearray.fromhex('fa4be61248798a06647847c466d484f2')
    BTADD_P  = bytearray.fromhex('20819A076931')
    SRES  = bytearray.fromhex('17702cfd')

    ComputedSRES = la(K, C_V, BTADD_P)
    log.debug("Challenge: {}, Response: {}".format(repr(C_V), repr(SRES)))
    assert ComputedSRES == SRES


if __name__ == "__main__":

    test_la()
