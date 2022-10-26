import tkinter as tk
from tkinter import messagebox
import os
from PIL import ImageTk, Image

mainscreen=tk.Tk()
mainscreen.geometry('950x600')
mainscreen.resizable(False,False)
mainscreen.title("UI Builder")

'''menubar=tk.Menu(mainscreen)
menubar.add_command(label="File")
menubar.add_cascade(label="Hello")
mainscreen.config(menu=menubar)

'''

def on_logout():
    mainscreen.quit()

def changepass():


    def info():

        '''


        need to add backend


        '''
        messagebox.showinfo("UI Builder","Password Updated!")

    top = tk.Toplevel(mainscreen)
    top.geometry("500x250")
    top.resizable(0,0)
    top.title("Change Password")
    top['bg']="#2b72cf"
    lab_UI = tk.Label(top,text="UI Builder", font=('Bahnschrift', 24), bg="#2b72cf", fg='white')
    lab_UI.place(x=330, y=5)

    old_lab=tk.Label(top,   text="Old password          :", font=('Bahnschrift', 14), bg="#2b72cf", fg='white')
    old_lab.place(x=30,y=80)
    new_lab = tk.Label(top, text="New password        :", font=('Bahnschrift', 14), bg="#2b72cf", fg='white')
    new_lab.place(x=30, y=120)
    ren_lab = tk.Label(top, text="Re-Enter password :", font=('Bahnschrift', 14), bg="#2b72cf", fg='white')
    ren_lab.place(x=30, y=160)
    old_in = tk.Entry(top, border=0, font=('Bahnschrift', 14,), fg='white', bg='#2a7ce8')
    old_in.place(x=240, y=82)
    new_in = tk.Entry(top, border=0, font=('Bahnschrift', 14,), fg='white', bg='#2a7ce8')
    new_in.place(x=240, y=122)
    ren_in = tk.Entry(top, border=0, font=('Bahnschrift', 14,), fg='white', bg='#2a7ce8')
    ren_in.place(x=240, y=162)

    upd_button=tk.Button(top,text="Update Password",border=0,command=info,font=('Bahnschrift', 14,), bg='white', fg='#2a7ce8')
    upd_button.place(x=200,y=205)




top_frame=tk.Frame(mainscreen,bg='#2b72cf',height=80,width=950)
top_frame.place(x=0,y=0)

left_frame=tk.Frame(mainscreen,bg='#224361',height=520,width=250)
left_frame.place(x=0,y=85)

'''

In Left Frame

'''




'''

In top frame

'''
lab_UI=tk.Label(text="UI Builder",font=('Bahnschrift',24),bg="#2b72cf",fg='white')
lab_UI.place(x=780,y=20)

lab_Uname=tk.Label(text="Welcome, username!",font=('Bahnschrift',20),bg="#2b72cf",fg='white')
lab_Uname.place(x=20,y=5)

logout=tk.Button(mainscreen,text="Logout", font=('Bahnschrift',12),command=on_logout,border=0,bg="#2b72cf",fg='white')
logout.place(x=20,y=45)

changepass=tk.Button(mainscreen,text="Change Password",command=changepass, font=('Bahnschrift',12),border=0,bg="#2b72cf",fg='white')
changepass.place(x=100,y=45)

mainscreen.mainloop()