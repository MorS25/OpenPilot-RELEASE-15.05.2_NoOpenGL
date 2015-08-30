#!/usr/bin/ruby
require 'socket'
s = UDPSocket.new
bytes = [42, 1, 1, 1, 1, 36].pack('G*')
s.send(bytes, 0, 'localhost', 2323)

