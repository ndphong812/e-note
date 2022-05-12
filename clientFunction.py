#Import thu vien
import socket
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.messagebox import askyesno
from clientGUI import *

#Ham khoi tao client
def initClient():
    global HOST
    global SERVER_PORT
    global FORMAT
    global FORMAT
    global client
    HOST = socket.gethostbyname(socket.gethostname())
    SERVER_PORT = 65432
    FORMAT = "utf8"
    global client
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
