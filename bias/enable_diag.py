import socket

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_RAW, socket.BTPROTO_HCI)
s.bind((0,))
s.send(b"\x07\xf0\x01")
s.close()
