# Import cac thu vien
import socket
import threading
from tkinter import *
import tkinter
import os
import json
import requests
import datetime
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.messagebox import askyesno

from fileinput import filename
import uuid

# Ham kiem tra tai khoan dang ki


def checkAccountRegister(username, password):
    existUsername = 0
    file_path = "data.json"
    fileEmpty = 0
    if os.stat(file_path).st_size == 0:
        fileEmpty = 1
    if fileEmpty == 1:
        existUsername = 0
    else:
        with open("data.json", 'r') as openfile:
            data_1 = json.load(openfile)
        for x in data_1["user"]:
            if(x["username"] == username):
                existUsername = 1

    if existUsername == 0:
        id = uuid.uuid1()
        strId = str(id)
        data = {
            "id": strId,
            "username": username,
            "password": password,
            "note": []
        }
        with open("data.json", "r+") as file_json:
            file_data = json.load(file_json)
            file_data["user"].append(data)
            file_json.seek(0)
            json.dump(file_data, file_json, indent=4)
    return existUsername

# Ham nhan thong tin dang ki


def handleRegister(conn: socket):
    conn.send("OK".encode(FORMAT))
    username = None
    password = None
    while(username != "" and password != ""):
        username = conn.recv(1024).decode(FORMAT)
        password = conn.recv(1024).decode(FORMAT)
        successRegister = checkAccountRegister(username, password)
        conn.sendall(str(successRegister).encode(FORMAT))
        HandleClient(conn, addr)

# Ham kiem tra tai khoan dang nhap


def checkAccountLogin(username, password):
    successLogin = 0
    if os.stat("data.json").st_size != 0:
        data = ""
        with open("data.json") as file_name:
            data = json.load(file_name)
        for x in data["user"]:
            if(x["username"] == username and x["password"] == password):
                successLogin = 1
    return successLogin


def handleLogin(conn: socket):
    conn.send("OK".encode(FORMAT))
    username = None
    password = None
    while(username != "" and password != ""):
        username = conn.recv(1024).decode(FORMAT)
        password = conn.recv(1024).decode(FORMAT)
        successLogin = checkAccountLogin(username, password)
        conn.sendall(str(successLogin).encode(FORMAT))
        HandleClient(conn, addr)

# Hanle add text


def handleAddText(conn: socket):
    conn.send("OK".encode(FORMAT))
    user_name_content = None
    text_content = None
    while(user_name_content != "" and text_content != ""):
        user_name_content = conn.recv(1024).decode(FORMAT)
        text_content = conn.recv(1024).decode(FORMAT)
        if os.stat("data.json").st_size != 0:
            data = ""
            with open("data.json", "r+") as file_name:
                data = json.load(file_name)
                for idx, x in enumerate(data["user"]):
                    if(x["username"] == user_name_content):
                        data["user"][idx]["note"].append({'id': str(uuid.uuid1()),
                                                          "type": "text", "content": text_content})
                file_name.seek(0)
                json.dump(data, file_name, indent=4)
        HandleClient(conn, addr)
# Ham tuong tac voi Client


def handleAddImage(conn: socket):
    conn.send("OK".encode(FORMAT))
    user_name_content = None
    while(user_name_content != ""):
        user_name_content = conn.recv(1024).decode(FORMAT)
        if os.stat("data.json").st_size != 0:
            data = ""
            with open("data.json", "r+") as file_name:
                data = json.load(file_name)
                for idx, x in enumerate(data["user"]):
                    if(x["username"] == user_name_content):
                        nameImage = str(user_name_content) + "_" + \
                            str(len(data["user"][idx]["note"])) + ".png"
                        data["user"][idx]["note"].append({'id': str(uuid.uuid1()),
                                                          "type": "image", "content": nameImage})
                file_name.seek(0)
                json.dump(data, file_name, indent=4)

        file = open(nameImage, "wb")
        image_chunk = conn.recv(2048)  # stream-based protocol
        while image_chunk:
            file.write(image_chunk)
            image_chunk = conn.recv(2048)
        file.close()
        HandleClient(conn, addr)


def handleAddFile(conn: socket):
    conn.send("OK".encode(FORMAT))
    user_name_content = None
    while(user_name_content != ""):
        user_name_content = conn.recv(1024).decode(FORMAT)
        SEPARATOR = "<SEPARATOR>"
        BUFFER_SIZE = 1024 * 10000
        received = conn.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename)
        filesize = int(filesize)
        type = filename.split('.')
        if os.stat("data.json").st_size != 0:
            data = ""
            with open("data.json", "r+") as file_name:
                data = json.load(file_name)
                for idx, x in enumerate(data["user"]):
                    if(x["username"] == user_name_content):
                        filename1 = str(user_name_content) + "_" + \
                            str(len(data["user"][idx]["note"])) + \
                            "." + str(type[1])
                        data["user"][idx]["note"].append({'id': str(uuid.uuid1()),
                                                          "type": "file", "content": filename1})
                file_name.seek(0)
                json.dump(data, file_name, indent=4)
        with open(filename1, "wb") as f:
            while True:
                bytes_read = conn.recv(BUFFER_SIZE)
                if not bytes_read:
                    break
                f.write(bytes_read)
        HandleClient(conn, addr)


def handleView(conn: socket):
    conn.send("OK".encode(FORMAT))
    username = None
    while(username != ""):
        username = conn.recv(1024).decode(FORMAT)
        if os.stat("data.json").st_size != 0:
            data = ""
            with open("data.json", "r+") as file_name:
                data = json.load(file_name)
                for idx, x in enumerate(data["user"]):
                    if(x["username"] == username):
                        lengthNote = str(len(data["user"][idx]["note"]))
                        conn.send(lengthNote.encode())
        HandleClient(conn, addr)


def handleViewDetail(conn: socket):
    conn.send("OK".encode(FORMAT))
    username = None
    index = None
    while(username != "" and index != ""):
        username = conn.recv(1024).decode(FORMAT)
        index = int(conn.recv(1024).decode(FORMAT))
        if os.stat("data.json").st_size != 0:
            data = ""
            with open("data.json", "r+") as file_name:
                data = json.load(file_name)
                for idx, x in enumerate(data["user"]):
                    if(x["username"] == username):
                        conn.send(data["user"][idx]["note"]
                                  [index]["content"].encode(FORMAT))
        HandleClient(conn, addr)


def HandleClient(conn: socket, addr):
    global username
    global password
    global method
    method = None
    while(method != ""):
        method = conn.recv(1024).decode(FORMAT)
        if(method == "register"):
            handleRegister(conn)
        if(method == "login"):
            handleLogin(conn)
        if(method == "add_text"):
            handleAddText(conn)
        if(method == "add_file"):
            handleAddFile(conn)
        if(method == "add_image"):
            handleAddImage(conn)
        if(method == "view"):
            handleView(conn)
        if(method == "view-detail"):
            handleViewDetail(conn)
    conn.close()

# Ham khoi tao Server


def initServer():
    global data
    data = {}
    data['user'] = []
    global HOST
    global FORMAT
    global SERVER_PORT
    global s
    HOST = socket.gethostbyname(socket.gethostname())
    SERVER_PORT = 65432
    FORMAT = "utf8"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, SERVER_PORT))
    s.listen()

# Ham ket noi den Client


def connectClient():
    while(1):
        try:
            global conn
            global addr
            conn, addr = s.accept()
            thr = threading.Thread(target=HandleClient, args=(conn, addr))
            thr.daemon = True
            thr.start()
        except:
            pass


def serverScreen():

    initServer()
    global main_screen_server
    main_screen_server = Tk()
    main_screen_server.geometry("800x500")
    main_screen_server.title("TCP Server")
    main_screen_server.configure(bg='#556677')
    Label(text="MÀN HÌNH SERVER", fg="white", bg="#3398cc",
          width="300", height="2", font=("sans-serif", 14)).pack()
    Button(text="RUN", cursor="heart", fg="white", height="1", bg="#3398cc",
           width="10", font=("sans-serif", 10), command=connectClient).place(x=30, y=100)
    Label(main_screen_server, text="IP Adress:" + str(HOST), fg="white",
          font=("sans-serif", 12), bg='#556677').place(x=300, y=100)
    Label(main_screen_server, text="PORT:" + str(SERVER_PORT), fg="white", font=(
        "sans-serif", 12), bg='#556677').place(x=600, y=100)
    main_screen_server.mainloop()


serverScreen()
input()

s.close()
