# Import thu vien
import socket
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.messagebox import askyesno
import os
import json
# Ham dang ki tai khoan


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
    repassword = StringVar()
    Label(register_screen, text="Nhập thông tin", fg="white",
          font=("sans-serif", 12), bg='#556677').pack()
    Label(register_screen, text="", bg='#556677').pack()

    # Label Ten tai khoan
    username_lable = Label(register_screen, text="Tên tài khoản:",
                           fg="white", font=("sans-serif", 10), bg='#556677')
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username,
                           bg="#c0c0c0", font=("sans-serif", 10), justify=CENTER)
    username_entry.focus_force()
    username_entry.pack(side=TOP, ipadx=30, ipady=6)

    # Label mat khau
    password_lable = Label(register_screen, text="Mật khẩu: ",
                           fg="white", font=("sans-serif", 10), bg='#556677')
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password,
                           show='*', bg="#c0c0c0", font=("sans-serif", 10), justify=CENTER)
    password_entry.focus_force()
    password_entry.pack(side=TOP, ipadx=30, ipady=6)

    # Label xac nhan mat khau
    repassword_lable = Label(register_screen, text="Xác nhận mật khẩu: ",
                             fg="white", font=("sans-serif", 10), bg='#556677')
    repassword_lable.pack()
    repassword_entry = Entry(register_screen, textvariable=repassword,
                             show='*', bg="#c0c0c0", font=("sans-serif", 10), justify=CENTER)
    repassword_entry.focus_force()
    repassword_entry.pack(side=TOP, ipadx=30, ipady=6)
    Label(register_screen, text="", bg='#556677').pack()
    Button(register_screen, text="Đăng ký", fg="white", width=10,
           height=1, bg="#3398cc", command=register_user).pack()


# Ham kiem tra dang ki
def register_user():
    global username_info
    global password_info
    username_info = username.get()
    password_info = password.get()
    repassword_info = repassword.get()
    if(len(username_info) < 5 or username_info.isalnum() == False):
        label = Label(register_screen, bg='#556677',
                      text="Tên tài khoản ít nhất 5 kí tự (a-z,0-9)", fg="orange", font=("sans-serif", 11))
        label.pack()
        label.after(2000, lambda: label.destroy())
    else:
        if(len(password_info) < 3):
            label = Label(register_screen, bg='#556677', fg="orange",
                          text="Mật khẩu ít nhất 3 kí tự", font=("sans-serif", 11))
            label.pack()
            label.after(2000, lambda: label.destroy())
        else:
            if(repassword_info != password_info):
                label = Label(register_screen, bg='#556677', fg="orange",
                              text="Mật khẩu xác nhận không chính xác", font=("sans-serif", 11))
                label.pack()
                label.after(2000, lambda: label.destroy())
            else:
                client.sendall("register".encode(FORMAT))
                replyRes = client.recv(1024).decode(FORMAT)
                if(replyRes == "OK"):
                    client.sendall(username_info.encode(FORMAT))
                    client.sendall(password_info.encode(FORMAT))
                    username_entry.delete(0, END)
                    password_entry.delete(0, END)
                    repassword_entry.delete(0, END)
                    notificationRegister()

# Ham thong bao tai khoan ton tai


def exist_user():
    label = Label(register_screen, bg='#556677', fg="orange",
                  text="Tên tài khoản đã tồn tại", font=("sans-serif", 11))
    label.pack()
    label.after(2000, lambda: label.destroy())


# Xuat ra ket qua dang ki tai khoan
def notificationRegister():
    successRegister = client.recv(1024).decode(FORMAT)
    if(successRegister == "0"):
        label = Label(register_screen, bg='#556677',
                      text="Đăng ký tài khoản thành công", fg="white", font=("sans-serif", 11))
        label.pack()
        label.after(2000, lambda: label.destroy())
    else:
        exist_user()


# Giao dien chinh dang nhap
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Đăng nhập")
    login_screen.geometry("500x300")
    login_screen.configure(bg='#556677')
    Label(login_screen, text="Điền thông tin đăng nhập",
          fg="white", font=("sans-serif", 10), bg='#556677').pack()
    Label(login_screen, text="", bg='#556677').pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Tên tài khoản: ", fg="white",
          font=("sans-serif", 10), bg='#556677').pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, bg="#c0c0c0", font=(
        "sans-serif", 10), justify=CENTER)
    username_login_entry.focus_force()
    username_login_entry.pack(side=TOP, ipadx=30, ipady=6)
    Label(login_screen, text="", bg='#556677').pack()
    Label(login_screen, text="Mật khẩu: ", fg="white",
          font=("sans-serif", 10), bg='#556677').pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, font=(
        "sans-serif", 10), show='*', bg="#c0c0c0", justify=CENTER)
    password_login_entry.focus_force()
    password_login_entry.pack(side=TOP, ipadx=30, ipady=6)
    Label(login_screen, text="", bg='#556677').pack()
    Button(login_screen, text="Đăng nhập", fg="white", font=("sans-serif",
           11), width=15, height=1, bg="#3398cc", command=login_verify).pack()


# Ham gui tai khoan mat khau di
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    client.sendall("login".encode(FORMAT))
    replyRes = client.recv(1024).decode(FORMAT)
    if(replyRes == "OK"):
        client.sendall(username1.encode(FORMAT))
        client.sendall(password1.encode(FORMAT))
        notificationLogin(username1)


# Ham xuat ra thong tin dang nhap
def notificationLogin(username):
    successLogin = client.recv(1024).decode(FORMAT)
    if(successLogin == "1"):
        login_sucess(username)
    else:
        label = Label(login_screen, fg="orange", bg='#556677',
                      text="Tài khoản hoặc mật khẩu không chính xác", font=("sans-serif", 12))
        label.pack()
        label.after(2000, lambda: label.destroy())

# Ham them Text Note


def addTextNote(username):
    global add_text_screen
    add_text_screen = Toplevel(main_screen)
    add_text_screen.title("Ghi chú")
    add_text_screen.geometry("500x300")
    add_text_screen.configure(bg='#556677')
    Label(add_text_screen, text="Điền thông tin",
          fg="white", font=("sans-serif", 10), bg='#556677').pack()
    Label(add_text_screen, text="", bg='#556677').pack()
    global text_verify
    text_verify = StringVar()
    global text_entry
    Label(add_text_screen, text="Nội dung: ", fg="white",
          font=("sans-serif", 10), bg='#556677').pack()
    text_entry = Entry(add_text_screen, textvariable=text_verify, bg="#c0c0c0", font=(
        "sans-serif", 10), justify=CENTER)
    text_entry.focus_force()
    text_entry.pack(side=TOP, ipadx=30, ipady=6)

    Label(add_text_screen, text="", bg='#556677').pack()
    Button(add_text_screen, text="Submit", fg="white", font=("sans-serif",
           11), width=15, height=1, bg="#3398cc", command=lambda: addTextToDataBase(username)).pack()


def addFilesNote(username):

    global add_file_screen
    add_file_screen = Toplevel(main_screen)
    add_file_screen.title("Ghi chú")
    add_file_screen.geometry("500x300")
    add_file_screen.configure(bg='#556677')
    Label(add_file_screen, text="Điền thông tin",
          fg="white", font=("sans-serif", 10), bg='#556677').pack()

    Label(add_file_screen, text="", bg='#556677').pack()
    global file_verify
    file_verify = StringVar()
    global file_entry
    Label(add_file_screen, text="Nội dung: ", fg="white",
          font=("sans-serif", 10), bg='#556677').pack()
    file_entry = Entry(add_file_screen, textvariable=file_verify, bg="#c0c0c0", font=(
        "sans-serif", 10), justify=CENTER)
    file_entry.focus_force()
    file_entry.pack(side=TOP, ipadx=30, ipady=6)

    Label(add_file_screen, text="", bg='#556677').pack()
    Button(add_file_screen, text="Submit", fg="white", font=("sans-serif",
           11), width=15, height=1, bg="#3398cc", command=lambda: addFileToDataBase(username)).pack()


def addImagesNote(username):
    global add_image_screen
    add_image_screen = Toplevel(main_screen)
    add_image_screen.title("Ghi chú")
    add_image_screen.geometry("500x300")
    add_image_screen.configure(bg='#556677')
    Label(add_image_screen, text="Điền thông tin",
          fg="white", font=("sans-serif", 10), bg='#556677').pack()
    Label(add_image_screen, text="", bg='#556677').pack()
    global image_verify
    image_verify = StringVar()
    global image_entry
    Label(add_image_screen, text="Đường dẫn ảnh: ", fg="white",
          font=("sans-serif", 10), bg='#556677').pack()
    image_entry = Entry(add_image_screen, textvariable=image_verify, bg="#c0c0c0", font=(
        "sans-serif", 10), justify=CENTER)
    image_entry.focus_force()
    image_entry.pack(side=TOP, ipadx=30, ipady=6)

    Label(add_image_screen, text="", bg='#556677').pack()
    Button(add_image_screen, text="Submit", fg="white", font=("sans-serif",
           11), width=15, height=1, bg="#3398cc", command=lambda: addImageToDataBase(username)).pack()


def addImageToDataBase(username):
    image_info = image_verify.get()
    file = open(str(image_info), 'rb')
    image_data = file.read(2048)
    client.sendall("add_image".encode(FORMAT))
    replyRes = client.recv(1024).decode(FORMAT)
    if(replyRes == "OK"):
        client.sendall(username.encode(FORMAT))
        while image_data:
            client.send(image_data)
            image_data = file.read(2048)
        file.close()
        image_entry.delete(0, END)


def addTextToDataBase(username):
    text_info = text_verify.get()
    client.sendall("add_text".encode(FORMAT))
    replyRes = client.recv(1024).decode(FORMAT)
    if(replyRes == "OK"):
        client.sendall(username.encode(FORMAT))
        client.sendall(text_info.encode(FORMAT))
        text_entry.delete(0, END)


def addFileToDataBase(username):
    filename = file_verify.get()
    filesize = os.path.getsize(filename)
    BUFFER_SIZE = 1024 * 10000
    client.sendall("add_file".encode(FORMAT))
    replyRes = client.recv(1024).decode(FORMAT)
    SEPARATOR = "<SEPARATOR>"
    if(replyRes == "OK"):
        client.sendall(username.encode(FORMAT))
        client.send(f"{filename}{SEPARATOR}{filesize}".encode())
        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                client.sendall(bytes_read)
        file_entry.delete(0, END)
# Ham login thanh cong - Chuyen sang trang tra cuu


def viewDetailNote(username, index):
    global view_detail_note_screen
    view_detail_note_screen = Toplevel(login_screen)
    view_detail_note_screen.title("Ứng dụng E-note")
    view_detail_note_screen.geometry("500x300")
    view_detail_note_screen.configure(bg='#556677')
    Label(view_detail_note_screen, text="Ghi chú của bạn: ", fg="white",
          font=("sans-serif", 10), bg='#556677').pack()

    client.sendall("view-detail".encode(FORMAT))
    replyRes = client.recv(1024).decode(FORMAT)
    if(replyRes == "OK"):
        client.sendall(username.encode(FORMAT))
        client.sendall(str(index).encode(FORMAT))
        contentNote = client.recv(1024).decode(FORMAT)
        Label(view_detail_note_screen, text=str(contentNote), fg="white",
              font=("sans-serif", 10), bg='#556677').pack()
        Button(view_detail_note_screen, text="Download", fg="white",
               bg="#3398cc", width=10, height=1).pack(pady=20)


def viewNote(username):

    print("View note is running")
    global view_note_screen
    view_note_screen = Toplevel(login_screen)
    view_note_screen.title("Ứng dụng E-note")
    view_note_screen.geometry("500x300")
    view_note_screen.configure(bg='#556677')
    Label(view_note_screen, text="Những ghi chú của bạn: ", fg="white",
          font=("sans-serif", 10), bg='#556677').pack()

    Label(view_note_screen, text="", fg="white",
          font=("sans-serif", 10), bg='#556677').pack()

    client.sendall("view".encode(FORMAT))
    replyRes = client.recv(1024).decode(FORMAT)
    if(replyRes == "OK"):
        client.sendall(username.encode(FORMAT))
        lengthNote = int(client.recv(1024).decode(FORMAT))
        if(lengthNote == 0):
            Label(view_note_screen, text="Không có ghi chú nào ", fg="white",
                  font=("sans-serif", 10), bg='#556677').pack()
        else:
            for index in range(lengthNote):
                Label(view_note_screen, text="Ghi chú" + str(index+1), fg="white",
                      font=("sans-serif", 10), bg='#556677').pack()
                Button(view_note_screen, text="Xem", fg="white",
                       bg="#3398cc", width=10, height=1, command=lambda: viewDetailNote(username, index)).pack(pady=20)


def login_sucess(username):
    global search_screen
    search_screen = Toplevel(login_screen)
    search_screen.title("Ứng dụng E-note")
    search_screen.geometry("500x300")
    search_screen.configure(bg='#556677')

    Label(search_screen, text="Chọn định dạng cần ghi chú: ", fg="white",
          font=("sans-serif", 10), bg='#556677').pack()

    Button(search_screen, text="Text", fg="white",
           bg="#3398cc", width=10, height=1, command=lambda: addTextNote(username)).pack(pady=20)

    Button(search_screen, text="Images", fg="white",
           bg="#3398cc", width=10, height=1, command=lambda: addImagesNote(username)).pack(pady=20)

    Button(search_screen, text="Files", fg="white",
           bg="#3398cc", width=10, height=1, command=lambda: addFilesNote(username)).pack(pady=20)

    Button(search_screen, text="Xem ghi chú của bạn", fg="white",
           bg="#3398cc", width=30, height=1, command=lambda: viewNote(username)).pack(pady=20)


def quitApp():
    main_screen.destroy()

# Trang chu Client


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("800x500")
    main_screen.title("Trang chủ")
    main_screen.configure(bg='#556677')
    Label(text="ỨNG DỤNG TRA CỨU TỶ GIÁ TIỀN TỆ", fg="white", bg="#3398cc",
          width="300", height="2", font=("sans-serif", 14)).pack()
    Label(text="", bg='#556677').pack()
    Label(text="ĐẠI HỌC QUỐC GIA THÀNH PHỐ HCM",
          fg="white", bg='#556677').pack()
    Label(text="TRƯỜNG ĐH KHOA HỌC TỰ NHIÊN", fg="white", bg='#556677').pack()
    Label(text="", bg='#556677').pack()
    image1 = Image.open("logo.png")
    image1 = image1.resize((80, 80), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)
    panel = Label(main_screen, image=image1)
    panel.image = image1
    panel.pack()
    Label(text="", bg='#556677').pack()
    Label(text="", bg='#556677').pack()
    Button(text="Đăng nhập ngay", cursor="heart", fg="white", height="2",
           bg="#3398cc", width="30", font=("sans-serif", 10), command=login).pack()
    Label(text="", bg='#556677').pack()
    Button(text="Chưa có tài khoản?", cursor="heart", fg="white", height="2",
           bg="#3398cc", width="30", font=("sans-serif", 10), command=register).pack()
    Label(text="", bg='#556677').pack()
    Button(main_screen, text="Thoát ứng dụng", cursor="heart", fg="white", height="2",
           bg="#3398cc", width="30", font=("sans-serif", 10), command=quitApp).pack()
    main_screen.mainloop()

# Ham khoi tao client


def initClient():
    global SERVER_PORT
    global FORMAT
    global FORMAT
    global client
    SERVER_PORT = 65432
    FORMAT = "utf8"
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def inputHOSTFunction():
    global IPScreen
    IPScreen = Tk()
    IPScreen.geometry("800x500")
    IPScreen.title("Client")
    IPScreen.configure(bg='#556677')
    global addrIP
    addrIP = StringVar()
    Label(text="ỨNG DỤNG GHI CHÚ", fg="white", bg="#3398cc",
          width="300", height="2", font=("sans-serif", 14)).pack()
    Label(text="", bg='#556677').pack()
    Label(text="ĐẠI HỌC QUỐC GIA THÀNH PHỐ HCM",
          fg="white", bg='#556677').pack()
    Label(text="TRƯỜNG ĐH KHOA HỌC TỰ NHIÊN", fg="white", bg='#556677').pack()
    Label(text="", bg='#556677').pack()
    image1 = Image.open("logo.png")
    image1 = image1.resize((80, 80), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)
    panel = Label(IPScreen, image=image1)
    panel.image = image1
    panel.pack()
    Label(text="", bg='#556677').pack()
    Label(text="", bg='#556677').pack()
    IPScreen_lable = Label(IPScreen, text="Nhập địa chỉ IP của Server cần kết nối: ",
                           fg="white", font=("sans-serif", 10), bg='#556677').pack()
    IP_entry = Entry(IPScreen, bg="#c0c0c0", textvariable=addrIP,
                     font=("sans-serif", 10), justify=CENTER)
    IP_entry.focus_force()
    IP_entry.pack(side=TOP, ipadx=30, ipady=6)
    Label(IPScreen, text="", bg='#556677').pack()
    Button(IPScreen, text="Kết nối", fg="white", width=10,
           height=1, bg="#3398cc", command=connectServer).pack()
    IPScreen.mainloop()

# Ham ket noi den server


def connectServer():
    try:
        label = Label(IPScreen, text="Connecting...", fg="white", bg='#556677')
        label.pack()
        client.connect((addrIP.get(), SERVER_PORT))
        global data
        data = {}
        data['user'] = []
        IPScreen.destroy()
        main_account_screen()
    except:
        label = Label(
            IPScreen, text="Không tìm thấy địa chỉ IP của Server", fg="white", bg='#556677')
        label.pack()
        label.after(2000, lambda: label.destroy())


initClient()
inputHOSTFunction()
