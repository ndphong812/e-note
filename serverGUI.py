#Import thu vien
import socket
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.messagebox import askyesno
from serverFunction import *



#Trang chu Server
def serverScreen():
    global main_screen_server
    main_screen_server = Tk()
    main_screen_server.geometry("1000x600")
    main_screen_server.title("TCP Server")
    main_screen_server.configure(bg='#556677')
    Label(text="MÀN HÌNH SERVER",fg="white", bg="#3398cc", width="300", height="2", font=("sans-serif", 14)).pack()
    Button(text="RUN",cursor="heart",fg="white", height="1", bg="#3398cc", width="10",font=("sans-serif", 10), command=mainFunction).place(x=30, y=100)
    Button(text="STOP", cursor="heart",fg="white", height="1",bg="#3398cc", width="10", font=("sans-serif", 10)).place(x=150, y=100)
    Button(main_screen_server, text="RESTART",cursor="heart", fg="white",height="1",bg="#3398cc", width="10", font=("sans-serif", 10)).place(x=270, y=100)
    Label(main_screen_server, text="IP Adress:192.168.160.1 ",fg="white", font=("sans-serif",12),bg='#556677').place(x=510, y=100)
    Label(main_screen_server, text="PORT:65432",fg="white", font=("sans-serif",12),bg='#556677').place(x=700, y=100)
    chatlogServer = Text(main_screen_server, bg='white')
    chatlogServer.config(state=DISABLED)
    chatlogServer.place(x=6, y=150, height=386, width=480)
    chatlogClient = Text(main_screen_server, bg='white')
    chatlogClient.config(state=DISABLED)
    chatlogClient.place(x=510, y=150, height=386, width=480)
    main_screen_server.mainloop()
def mainFunction():
    initServer()
    crawlData()
    connectClient()
