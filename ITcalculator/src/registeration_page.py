from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import mysql.connector

r_window = Tk()
r_window.title("Registration window")
r_window.geometry("900x550+0+0")
r_window.config(bg="white")


def clear():
    txt_f_name.delete(0, END)
    txt_l_name.delete(0, END)
    txt_contact_no.delete(0, END)
    txt_email.delete(0, END)
    cmb_questions.current(0)
    txt_answer.delete(0, END)
    txt_password.delete(0, END)
    txt_c_password.delete(0, END)


def sign_in():
    r_window.destroy()
    import login_page


def register_data():
    if txt_f_name.get() == "" or txt_contact_no.get() == "" or txt_email.get() == "" or cmb_questions.get() == "Select" or txt_answer.get() == "" or txt_password.get() == "" or txt_c_password.get() == "":
        mb.showerror(title='Error', message="All fields must be filled!", icon='warning')
    elif txt_password.get() != txt_c_password.get():
        mb.showerror(title='Error', message="Password and Confirm Password doesn't match!", icon='warning')
    elif chk_var.get() != 1:
        mb.showerror(title='Error',
                     message="Please learn a bit about Tax before using this application. If you understand tax system then click the checkbutton and register.",
                     icon='warning')
    else:
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Prasanna@01",
                database="IT_Calculator"
            )
            cur = db.cursor()
            sql_select_query = "SELECT * from Users_info WHERE Email = %s"
            cur.execute(sql_select_query, (txt_email.get(),))
            row = cur.fetchone()
            if row is not None:
                mb.showerror(title='Error', message="User email already exists, Please try with other email",
                             icon='warning')
            else:
                cur.execute(
                    "insert into Users_info (F_name,L_name,Contact_no,Email,Question,Answer,Password) values(%s,%s,%s,%s,%s,%s,%s)",
                    (txt_f_name.get(),
                     txt_l_name.get(),
                     txt_contact_no.get(),
                     txt_email.get(),
                     cmb_questions.get(),
                     txt_answer.get(),
                     txt_password.get()
                     ))
                db.commit()
                db.close()
                mb.showinfo(title='Success', message="Registered successfully")
                clear()
        except Exception as es:
            mb.showerror(title='Error', message=f"Error due to: {str(es)}", icon='warning')


# BG image

bg = Image.open("Images/bg4.jpg")
bg = bg.resize((925, 575), Image.ANTIALIAS)
test = ImageTk.PhotoImage(bg)

bg1 = Label(image=test)
bg1.image = test
bg1.place(x=0, y=0, relwidth=1, relheight=1)

# FG image

fg = Image.open("Images/fg.png")
fg = fg.resize((350, 400), Image.ANTIALIAS)
test1 = ImageTk.PhotoImage(fg)

fg1 = Label(image=test1)
fg1.image = test1
fg1.place(x=70, y=75, width=270, height=400)

# Registration frame

r_frame = Frame(r_window, bg="white", borderwidth=1)
r_frame.place(x=340, y=75, width=500, height=400)

# Title
title = Label(r_frame, text="REGISTER HERE", font=("times new roman", 24, "bold"), bg="white", fg="green")
title.place(x=20, y=10)

# ----------------row1

# Label first name
f_name = Label(r_frame, text="First name", font=("times new roman", 18, "bold"), bg="white", fg="grey")
f_name.place(x=20, y=55)

txt_f_name = Entry(r_frame, font=("times new roman", 16), bg="lightgrey")
txt_f_name.place(x=20, y=85, width=200)

# Label last name
l_name = Label(r_frame, text="Last name", font=("times new roman", 18, "bold"), bg="white", fg="grey")
l_name.place(x=260, y=55)

txt_l_name = Entry(r_frame, font=("times new roman", 16), bg="lightgrey")
txt_l_name.place(x=260, y=85, width=200)

# ----------------row2

# Label contact no
contact_no = Label(r_frame, text="Contact No.", font=("times new roman", 18, "bold"), bg="white", fg="grey")
contact_no.place(x=20, y=115)

txt_contact_no = Entry(r_frame, font=("times new roman", 16), bg="lightgrey")
txt_contact_no.place(x=20, y=145, width=200)

# Label Email
email = Label(r_frame, text="Email", font=("times new roman", 18, "bold"), bg="white", fg="grey")
email.place(x=260, y=115)

txt_email = Entry(r_frame, font=("times new roman", 16), bg="lightgrey")
txt_email.place(x=260, y=145, width=200)

# ----------------row3

# Label questions
questions = Label(r_frame, text="Security Questions", font=("times new roman", 18, "bold"), bg="white", fg="grey")
questions.place(x=20, y=175)

cmb_questions = ttk.Combobox(r_frame, font=("times new roman", 14), state="readonly", justify=CENTER)
cmb_questions["values"] = ("Select", "Your Pet's name", "Your Nick name", "Your Best friend's name")
cmb_questions.current(0)
cmb_questions.place(x=20, y=205, width=200)

# Label answers
answer = Label(r_frame, text="Answer", font=("times new roman", 18, "bold"), bg="white", fg="grey")
answer.place(x=260, y=175)

txt_answer = Entry(r_frame, font=("times new roman", 16), bg="lightgrey")
txt_answer.place(x=260, y=205, width=200)

# ----------------row4

# Label password
password = Label(r_frame, text="Password", font=("times new roman", 18, "bold"), bg="white", fg="grey")
password.place(x=20, y=235)

txt_password = Entry(r_frame, font=("times new roman", 16), bg="lightgrey")
txt_password.place(x=20, y=265, width=200)

# Label confirm password
c_password = Label(r_frame, text="Confirm Password", font=("times new roman", 18, "bold"), bg="white", fg="grey")
c_password.place(x=260, y=235)

txt_c_password = Entry(r_frame, font=("times new roman", 16), bg="lightgrey")
txt_c_password.place(x=260, y=265, width=200)

# check button
chk_var = IntVar()
chk = Checkbutton(r_frame, text="I Understand Tax Systems", variable=chk_var, onvalue=1, offvalue=0, bg="white",
                  font=("times new roman", 16))
chk.place(x=20, y=305)

# register Button
btn_register = Button(r_frame, text="REGISTER NOW", font=("treko", 20, "bold"), cursor="hand2", bd=0, fg="#38a8ff",
                      command=register_data)
btn_register.place(x=170, y=345)

# sign in Label
l_in = Label(r_window, text="Already registered?", font=("times new roman", 18), bg="red", fg="white")
l_in.place(x=125, y=394)

# sign in Button
btn_login = Button(r_window, text="SIGN IN", font=("treko", 20, "bold"), bd=0, cursor="hand2", fg="red", command=sign_in)
btn_login.place(x=139, y=421, width=120)

r_window.mainloop()
