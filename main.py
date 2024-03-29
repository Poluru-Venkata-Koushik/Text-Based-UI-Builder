import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from twilio.rest import Client

mainscreen=tk.Tk()
mainscreen.geometry('950x600')
mainscreen.resizable(False,False)
mainscreen.title("UI Builder")

'''menubar=tk.Menu(mainscreen)
menubar.add_command(label="File")
menubar.add_cascade(label="Hello")
mainscreen.config(menu=menubar)

'''

def on_forgot():

    account_sid = 'ACbf48d4618102147aeae7e093832b3b09'
    auth_token = '392ba4b50afbee434db5fe49213f05b6'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG0f8d40b437f48ed64000f04312539f3f',
        body='How Can You Forget Your Password',
        to='+919491956708'
    )

    print(message.sid)


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
tabControl = ttk.Notebook(mainscreen)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Project 1')
tabControl.add(tab2, text='Project 2')
tabControl.place(x=250,y=80)

ttk.Label(tab1,
          text="Project 1",font=('Bahnschrift', 14,)).grid(column=0,row=0,padx=320,pady=250)
ttk.Label(tab2,
          text="Project 2",font=('Bahnschrift', 14,)).grid(column=0,row=0,padx=320,pady=250)

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