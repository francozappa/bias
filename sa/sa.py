"""
sa.py

Bluetooth BR/EDR secure (mutual) authentication procedure.

"""

from h4 import *
from h5 import *
log.setLevel(logging.INFO)


def sa(K, C_M, C_S, BTADD_M, BTADD_S):
    """Generate secure authentication response

        K shared long term key, 16 byte

        C_M master challenge, 16 byte

        C_S slave challenge, 16 byte

        BTADD_M master address

        BTADD_S slave address

        Returns SRES_M and SRES_S, 4 byte


    """

    K.reverse()

    Hash, K_A = h4(K, BTADD_M, BTADD_S, KeyID['btdk'])

    C_M.reverse()
    C_S.reverse()
    Hash, SRES_M, SRES_S, ACO = h5(K_A, C_M, C_S)

    SRES_M.reverse()
    SRES_S.reverse()

    return SRES_M, SRES_S


