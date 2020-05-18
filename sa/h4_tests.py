"""
h4_tests.py, page 1615

W = T = link key

A1, A2 are swapped

"""

from h4 import *
from constants import *
log.setLevel(logging.DEBUG)


def test_h4_1():

    # NOTE: in the test vector indicate with W
    T = bytearray.fromhex('c234c1198f3b520186ab92a2f874934e')
    A1    = bytearray.fromhex('56123737bfce')
    A2    = bytearray.fromhex('a713702dcfc1')

    ComputedHash, ComputedDAK = h4(T, A1, A2, KeyID['btdk'])

    Hash = bytearray.fromhex('b089c4e39d7c192c3aba3c2109d24c0dc039e700adf3a263008e65a8b00fb1fa')
    DAK = bytearray.fromhex('b089c4e39d7c192c3aba3c2109d24c0d')

    emsg1 = 'test_h4_1: Hash {} != {}'.format(repr(Hash), repr(ComputedHash))
    emsg2 = 'test_h4_1: DAK  {} != {}'.format(repr(DAK), repr(ComputedDAK))
    assert Hash == ComputedHash, emsg1
    assert DAK ==  ComputedDAK, emsg2



if __name__ == "__main__":

    print('')
    test_h4_1()
