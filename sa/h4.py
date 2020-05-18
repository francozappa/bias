#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
h4.py

With Secure Connections, a device authentication key is created using function
h4. The definition of the device authentication key generation function makes
use of the MAC function HMAC based on SHA-256, which is denoted as
HMAC-SHA-256 T with 128-bit key T. (pag 1699)

"""

from constants import *
log.setLevel(logging.DEBUG)

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac


def h4(T, A1, A2, KeyID):
    """Device Authentication Key (DAK) Generation for Secure Connections.

        T is a 16 byte key, e.g. the link key derived from f2

        A1 is the BTADD of the master, 6 bytes

        A2 is the BTADD of the slave, 6 bytes

        KeyID is an encoding of "btdk"

        Returns Hash, DAK
            DAK is used an input for h5

    """
    assert len(T) == 16 and type(T) == bytearray
    assert len(A1) == 6 and type(A1) == bytearray
    assert len(A2) == 6 and type(A2) == bytearray

    Hash = bytearray(32)
    DAK = bytearray(16)

    h = hmac.HMAC(T, hashes.SHA256(), backend=default_backend())

    message = bytearray()
    message.extend(KeyID)
    message.extend(A1)
    message.extend(A2)
    assert len(message) == 4 + 6 + 6
    h.update(message)

    Hash = bytearray(h.finalize())
    DAK = Hash[:16]

    return Hash, DAK
