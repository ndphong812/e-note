#Import cac thu vien
import socket
import threading
from tkinter import *
import os
import json
import requests
import datetime
import time
from clientGUI import connectServer
import schedule
import time

#Ham kiem tra tai khoan dang ki
def checkAccountRegister(username,password):
    existUsername=0
    file_path="data.json"
    fileEmpty=0
    if os.stat(file_path).st_size == 0:
        fileEmpty=1
    if fileEmpty==1:
        existUsername=0
    else:
        with open("data.json", 'r') as openfile:
            data_1 = json.load(openfile)
        for x in data_1["user"]:
            if(x["username"]==username):
                existUsername=1
    if existUsername==0:
        data={"username":username,"password":password}
        with open("data.json","r+") as file_json:
            file_data=json.load(file_json)
            file_data["user"].append(data)
            file_json.seek(0)
            json.dump(file_data,file_json, indent=4) 
    return existUsername

#Ham nhan thong tin dang ki
def handleRegister(conn:socket):
    conn.send("OK".encode(FORMAT))
    username=None
    password=None
    while(username!="" and password!=""):
        username=conn.recv(1024).decode(FORMAT)
        password=conn.recv(1024).decode(FORMAT)
        successRegister=checkAccountRegister(username,password)
        conn.sendall(str(successRegister).encode(FORMAT))
        HandleClient(conn,addr)

#Ham kiem tra tai khoan dang nhap
def checkAccountLogin(username,password):
    successLogin=0
    if os.stat("data.json").st_size != 0:
        data=""
        with open("data.json") as file_name:
            data=json.load(file_name)
        for x in data["user"]:
            if(x["username"]==username and x["password"]==password):
                successLogin=1
    return successLogin

#Ham tim kiem dong tien
def findMoney():
    Day=datetime.date.today()
    with open(rf"dataMoney-{Day}.json") as file_json:
        Money=json.load(file_json)
    data_Object=Money["items"]
    hasMoney=False
    for i in range(len(data_Object)):
        if(keyword==data_Object[i]["type"]):
            infoMoney=data_Object[i]["bantienmat"]+data_Object[i]["muatienmat"] +data_Object[i]["muack"]+data_Object[i]["banck"]
            conn.sendall(infoMoney.encode(FORMAT))
            hasMoney=True
    if(hasMoney==False):
        conn.sendall("Đồng tiền không tồn tại".encode(FORMAT))

#Ham crawl du lieu
def crawlData():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    url_page="https://www.dongabank.com.vn/exchange/export"
    data=requests.get(url_page,headers)
    y=data.content.decode(FORMAT)
    y=y[:-1]
    y=y[1:]
    dataMoney=json.loads(y)
    Day=datetime.date.today()
    with open(rf"dataMoney-{Day}.json","w") as file_json:
        json.dump(dataMoney,file_json, indent=4) 
        file_json.write("\n")


#Ham xu ly tim kiem dong tien
def handleSearch():
    conn.send("OK".encode(FORMAT))
    global keyword
    keyword=None
    while(keyword!=""):
        keyword=conn.recv(1024).decode(FORMAT)
        findMoney()
        HandleClient(conn,addr)

#Ham nhan thong tin dang nhap
def handleLogin(conn: socket):
    conn.send("OK".encode(FORMAT))
    username=None
    password=None
    while(username!="" and password!=""):
        username=conn.recv(1024).decode(FORMAT)
        password=conn.recv(1024).decode(FORMAT)
        successLogin=checkAccountLogin(username,password)
        conn.sendall(str(successLogin).encode(FORMAT))
        HandleClient(conn,addr)

#Ham tuong tac voi Client
def HandleClient(conn: socket,addr):
    global username
    global password
    global method
    method=None
    while(method!=""):
        method=conn.recv(1024).decode(FORMAT)
        if(method=="register"):
            handleRegister(conn)
        if(method=="login"):
            handleLogin(conn)
        if(method=="search"):
            handleSearch()
    conn.close()

#Ham khoi tao Server
def initServer():
    global data
    data={}
    data['user']=[]
    global HOST
    global FORMAT
    global SERVER_PORT
    global s
    HOST = socket.gethostbyname(socket.gethostname())
    SERVER_PORT = 65432
    FORMAT = "utf8"
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,SERVER_PORT))
    s.listen()

#Ham ket noi den Client
def connectClient():
    
    while(1):
        try:
            global conn
            global addr
            conn ,addr = s.accept()
            thr = threading.Thread(target=HandleClient,args = (conn,addr))
            thr.daemon = True
            thr.start()

        except:
            pass
    
def autoGetData():
    schedule.every(5).seconds.do(crawlData)
    while True:
        schedule.run_pending()
        time.sleep(1)