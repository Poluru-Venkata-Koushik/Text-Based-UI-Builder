import tkinter as tk
from PIL import ImageTk, Image
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client['mydb']

collection = db['Fin']

details = collection.find()


def take_in():
    username = usernamein.get()
    password = passwordin.get()
    check_inp(username,password)


def check_inp(username,password):
    for detail in details:
        if detail['username'] == username and detail['password'] == password:
            '''
            DO SOMETHING
            '''
    '''
    DO SOMETHING ELSE
    '''







login_page=tk.Tk()
login_page.geometry('750x500')
login_page.resizable(False,False)
login_page.configure(bg='white')
login_page.title("UI Builder")
'''
img0 = ImageTk.PhotoImage(Image.open("D:\Project\logo.png"))
logo_lab = tk.Label(image = img0)
logo_lab.place(x=570,y=-3)'''

tc=tk.Label(text="Amrita Vishwa Vidyapeetham",font=('Bahnschrift',10),fg='gray',bg="white")
tc.place(x=560,y=475)
img = ImageTk.PhotoImage(Image.open("D:\Project\login.jpg"))
imgleft_lab = tk.Label(image = img)
imgleft_lab.place(x=-3,y=-3)

Welcome=tk.Label(text="Welcome to UI Builder",bg='white',font=('Bahnschrift',24),fg='#060C13')
Welcome.place(x=330,y=60)
Signintxt=tk.Label(text="Login/Register",bg='white',font=('Bahnschrift',18),fg='#0D6281')
Signintxt.place(x=400,y=145)
Usernametext=tk.Label(text="Username    :",bg='white',font=('Bahnschrift',13,),fg='#7A7A7A')
Usernametext.place(x=300,y=210)
usernamein=tk.Entry(login_page,border=0,font=('Bahnschrift',13,),fg='black',bg='#F6F6F6')
usernamein.place(x=420,y=213)
passwordtext=tk.Label(text="Password    :",bg='white',font=('Bahnschrift',13,),fg='#7A7A7A')
passwordtext.place(x=300,y=250)
passwordin=tk.Entry(login_page,border=0,font=('Bahnschrift',13,),fg='black',bg='#F6F6F6')
passwordin.place(x=420,y=253)
login_button = tk.Button(login_page, text="Log in",width=14, font=('Bahnschrift', 13,'bold'),border=0, bg='#086587',fg='#FCFCFC')
login_button.place(x=420, y=320)
fpwd_button = tk.Button(login_page, text="Forgot Password",font=('Bahnschrift', 12,'underline'),border=0, fg='black',bg='#FCFCFC')
fpwd_button.place(x=420, y=360)
noaccounttext=tk.Label(text="Don't Have an account?",bg='white',font=('Bahnschrift',13,),fg='#7A7A7A')
noaccounttext.place(x=300,y=420)
register_button = tk.Button(login_page, text="New User, Register Here!", font=('Bahnschrift', 13,'bold','underline'),border=0, fg='#332D2D',bg='#FCFCFC')
register_button.place(x=500, y=417)

login_page.mainloop()

