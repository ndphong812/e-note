# This is for clint
import socket
import time
c = socket.socket()
condition = True
c.connect(("localhost", 1234))
f = open("receive.png", "wb")
while condition:
    image = c.recv(1024)
    if str(image) == "b''":
        condition = False
    f.write(image)
print("Received")
