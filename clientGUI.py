#Import thu vien
import socket
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.messagebox import askyesno

#Ham dang ki tai khoan
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Đăng ký tài khoản")
    register_screen.geometry("500x300")
    register_screen.configure(bg='#556677')
    global username
    global password
    global repassword
    global username_entry
    global password_entry
    global repassword_entry
    username = StringVar()
    password = StringVar()
    repassword=StringVar()
    Label(register_screen, text="Nhập thông tin",fg="white", font=("sans-serif",12),bg='#556677').pack()
    Label(register_screen, text="",bg='#556677').pack()

    #Label Ten tai khoan
    username_lable = Label(register_screen, text="Tên tài khoản:",fg="white", font=("sans-serif",10),bg='#556677')
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username,bg="#c0c0c0", font=("sans-serif", 10),justify = CENTER)
    username_entry.focus_force()
    username_entry.pack(side = TOP, ipadx = 30, ipady = 6)

    #Label mat khau
    password_lable = Label(register_screen, text="Mật khẩu: ",fg="white", font=("sans-serif",10),bg='#556677')
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*',bg="#c0c0c0", font=("sans-serif", 10),justify = CENTER)
    password_entry.focus_force()
    password_entry.pack(side = TOP, ipadx = 30, ipady = 6)

    #Label xac nhan mat khau
    repassword_lable = Label(register_screen, text="Xác nhận mật khẩu: ",fg="white", font=("sans-serif",10),bg='#556677')
    repassword_lable.pack()
    repassword_entry = Entry(register_screen,textvariable=repassword,show='*',bg="#c0c0c0", font=("sans-serif", 10),justify = CENTER)
    repassword_entry.focus_force()
    repassword_entry.pack(side = TOP, ipadx = 30, ipady = 6)
    Label(register_screen, text="",bg='#556677').pack()
    Button(register_screen, text="Đăng ký", fg="white", width=10, height=1,bg="#3398cc", command = register_user).pack()
 
 
#Ham kiem tra dang ki
def register_user():
    global username_info
    global password_info
    username_info = username.get()
    password_info = password.get()
    repassword_info=repassword.get()
    if(username_info==""):
        label=Label(register_screen, bg='#556677',text="Tên tài khoản không được để trống", fg="orange", font=("sans-serif", 11))
        label.pack()
        label.after(2000 , lambda: label.destroy())
    else:
        if(password_info==""):
            label=Label(register_screen, bg='#556677',fg="orange",text="Mật khẩu không được để trống", font=("sans-serif", 11))
            label.pack()
            label.after(2000 , lambda: label.destroy())
        else:
            if(repassword_info!=password_info):
                label=Label(register_screen,bg='#556677',fg="orange", text="Mật khẩu xác nhận không chính xác", font=("sans-serif", 11))
                label.pack()
                label.after(2000 , lambda: label.destroy())
            else:
                client.sendall("register".encode(FORMAT))
                replyRes=client.recv(1024).decode(FORMAT)
                if(replyRes=="OK"):
                    client.sendall(username_info.encode(FORMAT))
                    client.sendall(password_info.encode(FORMAT))
                    username_entry.delete(0, END)
                    password_entry.delete(0, END)
                    repassword_entry.delete(0,END)
                    notificationRegister()

#Ham thong bao tai khoan ton tai
def exist_user():
    label=Label(register_screen,bg='#556677', fg="orange",text="Tên tài khoản đã tồn tại", font=("sans-serif", 11))
    label.pack()
    label.after(2000 , lambda: label.destroy())
    

#Xuat ra ket qua dang ki tai khoan
def notificationRegister():
    successRegister=client.recv(1024).decode(FORMAT)
    if(successRegister=="0"):
        label=Label(register_screen, bg='#556677',text="Đăng ký tài khoản thành công", fg="white", font=("sans-serif", 11))
        label.pack()
        label.after(2000 , lambda: label.destroy())
    else:
        exist_user()


#Giao dien chinh dang nhap
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Đăng nhập")
    login_screen.geometry("500x300")
    login_screen.configure(bg='#556677')
    Label(login_screen, text="Điền thông tin đăng nhập",fg="white", font=("sans-serif",10), bg='#556677').pack()
    Label(login_screen, text="",bg='#556677').pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Tên tài khoản: ",fg="white", font=("sans-serif",10),bg='#556677').pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, bg="#c0c0c0", font=("sans-serif", 10),justify = CENTER)
    username_login_entry.focus_force()
    username_login_entry.pack(side = TOP, ipadx = 30, ipady = 6)
    Label(login_screen, text="",bg='#556677').pack()  
    Label(login_screen, text="Mật khẩu: ",fg="white", font=("sans-serif",10),bg='#556677').pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, font=("sans-serif", 10), show= '*', bg="#c0c0c0", justify = CENTER)
    password_login_entry.focus_force()
    password_login_entry.pack(side = TOP, ipadx = 30, ipady = 6)
    Label(login_screen, text="", bg='#556677').pack()
    Button(login_screen, text="Đăng nhập",fg="white", font=("sans-serif",11), width=15, height=1,bg="#3398cc", command = login_verify).pack()
 

#Ham gui tai khoan mat khau di
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    client.sendall("login".encode(FORMAT))
    replyRes=client.recv(1024).decode(FORMAT)
    if(replyRes=="OK"):
        client.sendall(username1.encode(FORMAT))
        client.sendall(password1.encode(FORMAT))        
        notificationLogin()


#Ham xuat ra thong tin dang nhap
def notificationLogin():
    successLogin=client.recv(1024).decode(FORMAT)
    if(successLogin=="1"):
        login_sucess()
    else:
        label=Label(login_screen, fg="orange",bg='#556677',text="Tài khoản hoặc mật khẩu không chính xác", font=("sans-serif",12))
        label.pack()
        label.after(2000 , lambda: label.destroy())

#Ham tim kiem dong tien
def search():
    keyword=typeMoney.get()
    client.sendall("search".encode(FORMAT))
    replyRes=client.recv(1024).decode(FORMAT)
    if(replyRes=="OK"):
        client.sendall(keyword.encode(FORMAT))  
        value1=client.recv(1024).decode(FORMAT)
        if(value1!="Đồng tiền không tồn tại"):

            muatienmat=value1[0:5]
            bantienmat=value1[5:10]
            muack=value1[10:15]
            banck=value1[15:20]
            global label_money_1
            global label_money_2
            global label_money_3
            global label_money_4
            global label_money_5
            label_money_1=Label(search_screen, text="Giá mua tiền mặt: {} VNĐ".format(muatienmat), bg="#556677", fg="white")
            label_money_2=Label(search_screen, text="Giá bán tiền mặt: {} VNĐ".format(bantienmat), bg="#556677", fg="white")
            label_money_3=Label(search_screen, text="Giá mua chuyển khoản: {} VNĐ".format(muack), bg="#556677", fg="white")
            label_money_4=Label(search_screen, text="Giá bán chuyển khoản: {} VNĐ".format(banck), bg="#556677", fg="white")
            label_money_1.pack()
            label_money_2.pack()
            label_money_3.pack()
            label_money_4.pack()
            Label(search_screen, text="",fg="white", font=("sans-serif",10), bg='#556677').pack()
            
        else:
            label5=Label(search_screen, text="Đồng tiền không tồn tại", bg="#556677", fg="white")
            label5.pack()
            label5.after(2000 , lambda: label5.destroy())


def deleteSearch():
    label_money_1.destroy()
    label_money_2.destroy()
    label_money_3.destroy()
    label_money_4.destroy()
#Ham login thanh cong - Chuyen sang trang tra cuu 
def login_sucess():
    global search_screen
    search_screen = Toplevel(login_screen)
    search_screen.title("Bảng tra cứu tiền tệ")
    search_screen.geometry("500x300")
    search_screen.configure(bg='#556677')
    global typeMoney
    global typeMoney_entry
    typeMoney = StringVar()
    Label(search_screen, text="Nhập tên đồng tiền: ",fg="white", font=("sans-serif",10), bg='#556677').pack()
    typeMoney_entry = Entry(search_screen, textvariable=typeMoney, bg="#c0c0c0")
    typeMoney_entry.pack()
    Label(search_screen, text="",bg='#556677').pack()
    Button(search_screen, text="Tra cứu", fg="white",bg="#3398cc", width=10, height=1, command = search).pack()
    Label(search_screen, text="",fg="white", font=("sans-serif",10), bg='#556677').pack()
    # Button(search_screen, text="Xóa màn hình", fg="white",bg="#3398cc", width=10, height=1, command = deleteSearch).pack()

#Ham thoat ung dung
def quitApp():
    main_screen.destroy()
  
#Trang chu Client
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("800x500")
    main_screen.title("Trang chủ")
    main_screen.configure(bg='#556677')
    Label(text="ỨNG DỤNG TRA CỨU TỶ GIÁ TIỀN TỆ",fg="white", bg="#3398cc", width="300", height="2", font=("sans-serif", 14)).pack()
    Label(text="",bg='#556677').pack()
    Label(text="ĐẠI HỌC QUỐC GIA THÀNH PHỐ HCM", fg="white",bg='#556677').pack()
    Label(text="TRƯỜNG ĐH KHOA HỌC TỰ NHIÊN",fg="white",bg='#556677').pack()
    Label(text="",bg='#556677').pack()
    image1 = Image.open("logo.png")
    image1 = image1.resize((80, 80), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)
    panel = Label(main_screen, image=image1)
    panel.image = image1 
    panel.pack()
    Label(text="",bg='#556677').pack()
    Label(text="",bg='#556677').pack()
    Button(text="Đăng nhập ngay",cursor="heart",fg="white", height="2", bg="#3398cc", width="30",font=("sans-serif", 10), command = login).pack()
    Label(text="",bg='#556677').pack()
    Button(text="Chưa có tài khoản?", cursor="heart",fg="white", height="2",bg="#3398cc", width="30", font=("sans-serif", 10), command=register).pack()
    Label(text="",bg='#556677').pack()
    Button(main_screen, text="Thoát ứng dụng",cursor="heart", fg="white",height="2",bg="#3398cc", width="30", font=("sans-serif", 10), command=quitApp).pack()
    main_screen.mainloop()

#Ham khoi tao client
def initClient():
    global SERVER_PORT
    global FORMAT
    global FORMAT
    global client
    SERVER_PORT = 65432
    FORMAT = "utf8"
    global client
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def inputHOSTFunction():
    global IPScreen
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
    Button(IPScreen, text="Kết nối", fg="white", width=10, height=1,bg="#3398cc", command=connectServer).pack()
    IPScreen.mainloop()

#Ham ket noi den server
def connectServer():
    try:
        label=Label(IPScreen, text="Connecting...", fg="white",bg='#556677')
        label.pack()
        client.connect((addrIP.get(),SERVER_PORT))
        global data
        data={}
        data['user']=[]
        IPScreen.destroy()
        main_account_screen()
    except:
        label=Label(IPScreen, text="Không tìm thấy địa chỉ IP của Server", fg="white",bg='#556677')
        label.pack()
        label.after(2000 , lambda: label.destroy())