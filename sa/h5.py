#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
h5.py

With Secure Connections, device authentication confirmation values are
created using function h5. The definition of the device authentication
confirmation function makes use of the MAC function HMAC based on SHA-
256, which is denoted as HMAC-SHA-256 S with 128-bit key S.

page 1700

"""

from constants import *
log.setLevel(logging.DEBUG)

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac


def h5(S, R1, R2):
    """Device Authentication Key Confirmation for Secure Connections.

        S is the DAK computed from h4, 16 byte key

        R1 is the AURAND of the master, 16 bytes

        R2 is the AURAND of the slave, 16 bytes

        Returns Hash, SRESm, SRESs, and ACO
            SRESm, and SRESs are used in the secure authentication procedure
            ACO is used in h3 and as the IV for Encryption Start for the 
            encryption nonce.

    """
    assert len(S)  == 16 and type(S)  == bytearray
    assert len(R1) == 16 and type(R1) == bytearray
    assert len(R2) == 16 and type(R2) == bytearray

    Hash = bytearray(32)

    h = hmac.HMAC(S, hashes.SHA256(), backend=default_backend())

    message = bytearray()
    message.extend(R1)
    message.extend(R2)
    assert len(message) == 16 + 16
    h.update(message)

    Hash = bytearray(h.finalize())
    SRESm = Hash[:4]
    SRESs = Hash[4:8]
    ACO   = Hash[8:16]

    return Hash, SRESm, SRESs, ACO
