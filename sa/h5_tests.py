"""
h5_tests.py, page 1615

"""

from h5 import *
log.setLevel(logging.DEBUG)


def test_h5_1():

    R1    = bytearray.fromhex('d5cb8454d177733effffb2ec712baeab')
    R2    = bytearray.fromhex('a6e8e7cc25a75f6e216583f7ff3dc4cf')
    W    = bytearray.fromhex('b089c4e39d7c192c3aba3c2109d24c0d')
    DAK = W

    ComputedHash, ComputedSRESm, ComputedSRESs, ComputedACO = h5(DAK, R1, R2)

    Hash = bytearray.fromhex('746af87e1eeb1137c683b97d9d421f911f3ddf100403871b362958c458976d65')
    SRESm = bytearray.fromhex('746af87e')
    SRESs = bytearray.fromhex('1eeb1137')
    ACO = bytearray.fromhex('c683b97d9d421f91')

    emsg1 = 'test_h5_1: Hash {} != {}'.format(repr(Hash), repr(ComputedHash))
    assert Hash == ComputedHash, emsg1
    emsg2 = 'test_h5_1: SRESm {} != {}'.format(repr(SRESm), repr(ComputedSRESm))
    assert SRESm ==  ComputedSRESm, emsg2
    emsg3 = 'test_h5_1: SRESs {} != {}'.format(repr(SRESs), repr(ComputedSRESs))
    assert SRESs ==  ComputedSRESs, emsg3
    emsg4 = 'test_h5_1: ACO {} != {}'.format(repr(ACO), repr(ComputedACO))
    assert ACO ==  ComputedACO, emsg4



if __name__ == "__main__":

    print('')
    test_h5_1()
