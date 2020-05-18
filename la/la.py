"""
la.py

Bluetooth BR/EDR legacy (unilateral) authentication procedure.

"""

from e1 import *
log.setLevel(logging.INFO)


def la(K, C_V, BTADD_P):
    """Generate legacy authentication response

        K shared long term key, 16 byte

        C_V challenge from the verifier, 16 byte

        BTADD_P address of the prover (leftmost byte is MSB)

        Returns SRES, 4 byte


    """

    # NOTE: BTADD is processed in little endian
    BTADD_P.reverse()
    SRES, ACO = e1(K, C_V, BTADD_P)

    return SRES


if __name__ == "__main__":

    K   = bytearray.fromhex('159dd9f43fc3d328efba0cd8a861fa57')
    C_V  = bytearray.fromhex('bc3f30689647c8d7c5a03ca80a91eceb')
    BTADD_P  = bytearray.fromhex('7ca89b233c2d')
    SRES = la(K, C_V, BTADD_P)
    print("Challenge: {}, Response: {}".format(repr(C_V), repr(SRES)))

