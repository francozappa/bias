#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
constants.py

"""

from binascii import unhexlify, hexlify

import logging
log = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-4s %(levelname)-4s %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
# log.setLevel(logging.DEBUG)

KeyID = {
    'btdk': bytearray.fromhex('6274646b'),
}

def ba2hs(ba):
    return ''.join('{:02x}'.format(b) for b in ba)

