#!/usr/bin/python
import socket
import struct
from struct import *
data = [42, 1, 1, 1, 1, 36]
send = struct.pack("!dddddd", *data)
sock = socket.socket( socket.AF_INET,socket.SOCK_DGRAM )
sock.sendto(send,("localhost", 2323))

