import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 1234))
s.listen(5)

print("Server menunggu koneksi...")

clientsocket, address = s.accept()
print(f"Terhubung dengan {address}")

full_msg = b''
new_msg = True

while True:
    msg = clientsocket.recv(1024)
    if new_msg:
        msglen = int(msg[:HEADERSIZE])
        new_msg = False
    
    full_msg += msg

    if len(full_msg) - HEADERSIZE == msglen:
        print("File diterima!")
        break

file_data = full_msg[HEADERSIZE:]
with open("file_diterima", "wb") as f:
    f.write(file_data)

clientsocket.close()
