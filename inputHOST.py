from clientGUI import register


#Import thu vien
import socket
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.messagebox import askyesno
def inputHOSTFunction():

    IPScreen = Tk()
    IPScreen.geometry("800x500")
    IPScreen.title("Client")
    IPScreen.configure(bg='#556677')
    global addrIP
    addrIP=StringVar()

    Label(text="ỨNG DỤNG TRA CỨU TỶ GIÁ TIỀN TỆ",fg="white", bg="#3398cc", width="300", height="2", font=("sans-serif", 14)).pack()
    Label(text="",bg='#556677').pack()
    Label(text="ĐẠI HỌC QUỐC GIA THÀNH PHỐ HCM", fg="white",bg='#556677').pack()
    Label(text="TRƯỜNG ĐH KHOA HỌC TỰ NHIÊN",fg="white",bg='#556677').pack()
    Label(text="",bg='#556677').pack()
    image1 = Image.open("logo.png")
    image1 = image1.resize((80, 80), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)
    panel = Label(IPScreen, image=image1)
    panel.image = image1 
    panel.pack()
    Label(text="",bg='#556677').pack()
    Label(text="",bg='#556677').pack()

    IPScreen_lable = Label(IPScreen, text="Nhập địa chỉ IP của Server cần kết nối: ",fg="white", font=("sans-serif",10),bg='#556677').pack()

    IP_entry = Entry(IPScreen,bg="#c0c0c0",textvariable=addrIP, font=("sans-serif", 10),justify = CENTER)
    
    IP_entry.focus_force()
    IP_entry.pack(side = TOP, ipadx = 30, ipady = 6)

    Label(IPScreen, text="",bg='#556677').pack()
    Button(IPScreen, text="Kết nối", fg="white", width=10, height=1,bg="#3398cc").pack()

    IPScreen.mainloop()

inputHOSTFunction()