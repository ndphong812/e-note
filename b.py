# This is for socket
from tkinter import *
from tkinter import filedialog
import socket
c = 0
s = socket.socket()
s.bind(("localhost", 1234))
image = open("logo.png", "rb")
s.listen(1)
c, address = s.accept()
if c != 0:
    for i in image:
        c.send(i)
