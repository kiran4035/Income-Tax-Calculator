from tkinter import *
from tkinter import messagebox as mb
import mysql.connector
from PIL import Image, ImageTk

l_window = Tk()
l_window.title("login window")
l_window.geometry("900x550+0+0")


def register():
    l_window.destroy()
    import registeration_page


def current_user_id(user_id):
    return user_id


def login():
    if txt_email.get() == "" and txt_password.get() == "":
        mb.showerror(title='Error', message="Enter the registered email id and password to login!", icon='warning')
    elif txt_email.get() == "":
        mb.showerror(title='Error', message="Enter the registered email id!", icon='warning')
    elif txt_password.get() == "":
        mb.showerror(title='Error', message="Password required!", icon='warning')
    else:
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Prasanna@01",
                database="IT_Calculator"
            )
            cur = db.cursor()
            sql_select_query = "SELECT * from Users_info WHERE Email = %s and Password= %s"
            cur.execute(sql_select_query, (txt_email.get(), txt_password.get()))
            row = cur.fetchone()
            user_id_query = "SELECT User_id from Users_info WHERE Email = %s and Password= %s"
            cur.execute(user_id_query, (txt_email.get(), txt_password.get()))
            user_id = cur.fetchone()
            current_user_id(user_id)
            cur.close()
            if row is None:
                mb.showerror(title='Error', message="Invalid Email id/Password!!!", icon='warning')
            else:
                mb.showinfo(title='Success', message="Welcome")
                l_window.destroy()
                import main

        except Exception as es:
            mb.showerror(title='Error', message=f"Error due to: {str(es)}", icon='warning')


# background image

bgl = Image.open("Images/login_bg.png")
bgl = bgl.resize((900, 550), Image.ANTIALIAS)
test2 = ImageTk.PhotoImage(bgl)

bgl1 = Label(image=test2)
bgl1.image = test2
bgl1.place(x=0, y=0, relwidth=1, relheight=1)

# login frame

l_frame = Frame(l_window, bg="white", borderwidth=1)
l_frame.place(x=65, y=75, width=360, height=400)

# Title

title = Label(l_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="#1c94d9")
title.place(x=65, y=10)

# Label email

email = Label(l_frame, text="Email", font=("times new roman", 20, "bold"), bg="white", fg="black")
email.place(x=20, y=75)

txt_email = Entry(l_frame, font=("times new roman", 18), bg="lightgrey")
txt_email.place(x=20, y=110, width=300)

# Label password

password = Label(l_frame, text="Password", font=("times new roman", 20, "bold"), bg="white", fg="black")
password.place(x=20, y=165)

txt_password = Entry(l_frame, font=("times new roman", 18), bg="lightgrey")
txt_password.place(x=20, y=200, width=300)

# button register

btn_reg = Button(l_frame, text="Register New Account?", font=("times new roman", 16), bg="white", bd=0, cursor="hand2",
                 fg="#e0227b", command=register)
btn_reg.place(x=20, y=245)

# button login

btn_log = Button(l_frame, text="LOGIN", font=("treko", 20, "bold"), bg="#e0227b", cursor="hand2", bd=0, fg="#2faef7",
                 command=login)
btn_log.place(x=95, y=320, width=150, height=40)

l_window.mainloop()
