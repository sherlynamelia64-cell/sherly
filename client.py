import socket
import os

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1234))

filename = "contoh.jpg"

with open(filename, "rb") as f:
    data = f.read()

msg = bytes(f"{len(data):<{HEADERSIZE}}", "utf-8") + data
s.send(msg)

print("File berhasil dikirim")
s.close()