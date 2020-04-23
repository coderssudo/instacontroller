

import tkinter as tk
from inta_tools import *
import time
from PIL import ImageTk, Image
time.sleep(1)

insta = tk.Tk(className='Insta')
insta_img = ImageTk.PhotoImage(Image.open('/home/rai/Downloads/myicon.png'))
insta.geometry("200x200+300+300")
insta.resizable(width=False, height=False)
my_icon = tk.Label(image = insta_img)
my_icon.grid(row = "0", column = "0")
frame1 = tk.Frame(insta)
frame1.grid(row = "0", column = "1", padx = 10, pady=10)


def open_pic1():
    pic_open()

    frame2 = tk.Frame(insta, padx=50, pady=50)
    frame2.grid(row="0", column="1")

    frame3 = tk.Frame(frame2)
    frame3.grid(row="0", column="0")

    frame4 = tk.Frame(frame2)
    frame4.grid(row="1", column="0")

    def int_opt():
        frame2.destroy()
        option()

    def int_cross():
        frame2.destroy()
        cross_click()
        ser()

    label1 = tk.Label(frame3, text="Pic Opened ... Choose your Option", font='Helvetica 12 bold')
    label1.grid(row="0", column="0")

    like_button = tk.Button(frame4, text='Like', command=like)
    like_button.grid(row="0", column="0")

    save_button = tk.Button(frame4, text='Save', command=save)
    save_button.grid(row="0", column="1")

    close_button = tk.Button(frame4, text='Close Pic', command=int_cross)
    close_button.grid(row="1", column="0")

    back_button = tk.Button(frame4, text='Back', command=int_opt)
    back_button.grid(row="1", column="1")


def ser():
    frame2 = tk.Frame(insta, padx=50, pady=50)
    frame2.grid(row="0", column="1")

    frame3 = tk.Frame(frame2)
    frame3.grid(row="0", column="0")

    frame4 = tk.Frame(frame2)
    frame4.grid(row="1", column="0")

    def int_opt():
        frame2.destroy()
        option()

    def int_open_pic():
        frame2.destroy()
        open_pic1()

    def int_ser():
        search(user_name.get())
        open_pic = tk.Button(frame4, text='Open Pic', command=int_open_pic)
        open_pic.grid(row='0', column='1')

    label1 = tk.Label(frame3, text="Enter the id to Search", font='Helvetica 12 bold')
    label1.grid(row="0", column="0")

    user_name = tk.Entry(frame3, width=20)
    user_name.grid(row='1', column='0')

    search_button = tk.Button(frame3, text='Search', command=int_ser)
    search_button.grid(row="2", column="0")

    back_button = tk.Button(frame4, text='Back', command=int_opt)
    back_button.grid(row="0", column="0")


def log_out():
    logout()

    frame2 = tk.Frame(insta, padx=50, pady=50)
    frame2.grid(row="0", column="1")

    def int_opt():
        frame2.destroy()
        log()

    label1 = tk.Label(frame2, text="You have been LOGOUT", font='Helvetica 12 bold')
    label1.grid(row="0", column="0")

    back_button = tk.Button(frame2, text='Back', command=int_opt)
    back_button.grid(row="1", column="0")


def read():
    insta.geometry("400x400+300+300")
    insta.resizable(width=False, height=False)

    time.sleep(3)
    a = first_five_not()

    frame2 = tk.Frame(insta, padx=50, pady=50)
    frame2.grid(row="0", column="1")

    def int_opt():
        frame2.destroy()
        option()

    label1 = tk.Label(frame2, text="Here are your notifications", font='Helvetica 12 bold')
    label1.grid(row="0", column="0")

    label2 = tk.Label(frame2, text=a[0])
    label2.grid(row="1", column="0")

    label3 = tk.Label(frame2, text=a[1])
    label3.grid(row="2", column="0")

    label4 = tk.Label(frame2, text=a[2])
    label4.grid(row="3", column="0")

    label5 = tk.Label(frame2, text=a[3])
    label5.grid(row="4", column="0")

    label6 = tk.Label(frame2, text=a[4])
    label6.grid(row="5", column="0")

    back_button = tk.Button(frame2, text='Back', command=int_opt)
    back_button.grid(row="6", column="0")


def option():
    insta.geometry("400x200+300+300")
    insta.resizable(width=False, height=False)

    frame2 = tk.Frame(insta, padx=50, pady=50)
    frame2.grid(row="0", column="1")

    label1 = tk.Label(frame2, text="Welcome " + user + " Here are some Options", font='Helvetica 12 bold')
    label1.grid(row="0", column="0")

    def int_ser():
        frame2.destroy()
        ser()

    def int_logout():
        frame2.destroy()
        log_out()

    def int_read():
        frame2.destroy()
        read()

    #     label2 = tk.Label(frame2, text = "You have Loged In succefully")

    search_button = tk.Button(frame2, text='Search', command=int_ser)
    search_button.grid(row="1", column="0")

    logout_button = tk.Button(frame2, text='Logout', command=int_logout)
    logout_button.grid(row="2", column="0")

    read_button = tk.Button(frame2, text='Read Notification', command=int_read)
    read_button.grid(row="3", column="0")


def log():
    insta.geometry("400x200+300+300")
    insta.resizable(width=False, height=False)
    frame2 = tk.Frame(insta, padx=50, pady=50)
    frame2.grid(row="0", column="1")

    frame3 = tk.Frame(frame2)
    frame3.grid(row="0", column="0")

    frame4 = tk.Frame(frame2)
    frame4.grid(row="1", column="0")

    label = tk.Label(frame3, text='Hey...!!browser is ready ', font='Helvetica 12 bold')
    label.grid(row="0", column="0")

    label = tk.Label(frame4, text='User Name')
    label.grid(row="2", column="0")
    user_name = tk.Entry(frame4, width=20)
    user_name.grid(row='2', column='1')
    global user
    user = user_name.get()

    label = tk.Label(frame4, text='Password')
    label.grid(row="3", column="0")
    passw = tk.Entry(frame4, show="*", width=20)
    passw.grid(row='3', column='1')

    def int_option():
        login(user_name.get(), passw.get())
        option()
        frame2.destroy()

    log_button = tk.Button(frame4, text='login', width=10, command=int_option)
    log_button.grid(row="4", column="0")

    return user


def brow_but():
    def int_brow():
        frame1.destroy()
        brow()
        log()

    a = 'Open Browser'
    bro_button = tk.Button(frame1, text=a, command=int_brow)
    bro_button.grid(row="0", column="0")

brow_but()

insta.mainloop()
