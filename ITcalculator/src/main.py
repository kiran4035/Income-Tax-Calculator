from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import webbrowser
from calculate_tax import new_tax_calculation, old_tax_calculation
from calculate_surcharge import surcharge
from random_facts import random_fact
from FAQs import faqs
from history import history


# Create a window
root = Tk()

# App Title
root.title("Indian Income Tax calculator for Salaried Person")

# Create Paned window
panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL)
panedwindow.pack()

# Create Frames and specify its properties
frame1 = ttk.Frame(panedwindow, width=500, height=550, relief=RIDGE)
frame2 = ttk.Frame(panedwindow, width=400, height=550, relief=FLAT, padding="2m")
frame1.grid_propagate(0)
frame2.grid_propagate(0)
panedwindow.add(frame1, weight=1)
panedwindow.add(frame2, weight=1)

# Basic calculator section starts here....
# Specify Grid
Grid.columnconfigure(frame2, 0, weight=1)
Grid.columnconfigure(frame2, 1, weight=1)
Grid.columnconfigure(frame2, 2, weight=1)

Grid.rowconfigure(frame2, 0, weight=1)
Grid.rowconfigure(frame2, 1, weight=1)
Grid.rowconfigure(frame2, 2, weight=1)
Grid.rowconfigure(frame2, 3, weight=1)
Grid.rowconfigure(frame2, 4, weight=1)
Grid.rowconfigure(frame2, 5, weight=1)
Grid.rowconfigure(frame2, 6, weight=1)
Grid.rowconfigure(frame2, 7, weight=1)

# Creating Entry box and title for basic calculator
Label(frame2, text="Basic calculator", font=("Teko", 18, "bold")).grid(row=0, column=0, pady=0, columnspan=3)
user_input = Entry(frame2, width=42, font=("Teko", 18, "bold"), justify="right")
user_input.grid(row=1, column=0, columnspan=3, padx=0, pady=5, ipady=10, ipadx=10, sticky="NSEW")


def button_click(num):  # To display the number clicked
    current = user_input.get()
    user_input.delete(0, END)
    user_input.insert(0, str(current) + str(num))


def button_clear():  # To clear the content on the Entry box
    user_input.delete(0, END)


def button_equal():  # To do the arithmetic operation with the current and previously entered value
    second_num = user_input.get()
    user_input.delete(0, END)
    s_num = float(second_num)
    if math == "addition":
        user_input.insert(0, float(fa_num + s_num))
    elif math == "subtraction":
        user_input.insert(0, float(fs_num - s_num))
    elif math == "multiplication":
        user_input.insert(0, float(fm_num * s_num))
    elif math == "division":
        user_input.insert(0, float(fd_num / s_num))


def button_add():  # Add button
    first_num = user_input.get()
    global fa_num
    global math
    math = "addition"
    fa_num = float(first_num)
    user_input.delete(0, END)


def button_subtract():  # Subtract button
    first_num = user_input.get()
    global fs_num
    global math
    math = "subtraction"
    fs_num = float(first_num)
    user_input.delete(0, END)


def button_multiply():  # Multiplication button
    first_num = user_input.get()
    global fm_num
    global math
    math = "multiplication"
    fm_num = float(first_num)
    user_input.delete(0, END)


def button_divide():  # Division button
    global fd_num
    global math
    math = "division"
    first_num = user_input.get()
    fd_num = float(first_num)
    user_input.delete(0, END)


# defining buttons
button_1 = Button(frame2, text="1", padx=35, pady=20, font=("Teko", 18), command=lambda: button_click(1))
button_2 = Button(frame2, text="2", padx=35, pady=20, font=("Teko", 18), command=lambda: button_click(2))
button_3 = Button(frame2, text="3", padx=35, pady=20, font=("Teko", 18), command=lambda: button_click(3))
button_4 = Button(frame2, text="4", padx=35, pady=20, font=("Teko", 18), command=lambda: button_click(4))
button_5 = Button(frame2, text="5", padx=35, pady=20, font=("Teko", 18), command=lambda: button_click(5))
button_6 = Button(frame2, text="6", padx=35, pady=20, font=("Teko", 18), command=lambda: button_click(6))
button_7 = Button(frame2, text="7", padx=35, pady=20, font=("Teko", 18), command=lambda: button_click(7))
button_8 = Button(frame2, text="8", padx=35, pady=20, font=("Teko", 18), command=lambda: button_click(8))
button_9 = Button(frame2, text="9", padx=35, pady=20, font=("Teko", 18), command=lambda: button_click(9))
button_0 = Button(frame2, text="0", padx=35, pady=20, font=("Teko", 18), command=lambda: button_click(0))
button_add = Button(frame2, text="+", padx=35, pady=20, font=("Teko", 18), command=button_add)
button_subtract = Button(frame2, text="-", padx=47, pady=20, font=("Teko", 18), command=button_subtract)
button_multiply = Button(frame2, text="*", padx=47, pady=20, font=("Teko", 18), command=button_multiply)
button_divide = Button(frame2, text="/", padx=47, pady=20, font=("Teko", 18), command=button_divide)
button_equal = Button(frame2, text="=", padx=116, pady=20, font=("Teko", 18), command=button_equal)
button_clear = Button(frame2, text="Clear", padx=104, pady=20, font=("Teko", 18), command=button_clear)

# Putting button on the screen
button_1.grid(row=4, column=0, sticky="NSEW")
button_2.grid(row=4, column=1, sticky="NSEW")
button_3.grid(row=4, column=2, sticky="NSEW")

button_4.grid(row=3, column=0, sticky="NSEW")
button_5.grid(row=3, column=1, sticky="NSEW")
button_6.grid(row=3, column=2, sticky="NSEW")

button_7.grid(row=2, column=0, sticky="NSEW")
button_8.grid(row=2, column=1, sticky="NSEW")
button_9.grid(row=2, column=2, sticky="NSEW")

button_0.grid(row=5, column=0, sticky="NSEW")
button_multiply.grid(row=5, column=1, sticky="NSEW")
button_divide.grid(row=5, column=2, sticky="NSEW")

button_add.grid(row=6, column=0, sticky="NSEW")
button_clear.grid(row=6, column=1, columnspan=2, sticky="NSEW")

button_subtract.grid(row=7, column=0, sticky="NSEW")
button_equal.grid(row=7, column=1, columnspan=2, sticky="NSEW")


# Basic calculator section ends here....

# Welcome msg with suggestion
welcome_msg = '''
Welcome to India Income Tax Calculator
We encourage, you to learn about Tax Exemptions and Tax Deductions to reduce your Taxable income As 
much as possible.
"Have A nice day"'''
mb.showinfo(title='Welcome', message=welcome_msg, icon='warning')


# Tax calculation section starts here....
def clear_labels():  # To clear all the other labels while showing error
    lbl1.config(text="")
    lbl11.config(text="")
    lbl2.config(text="")
    lbl22.config(text="")
    lbl3.config(text="")
    lbl33.config(text="")
    lbl4.config(text="")
    lbl44.config(text="")
    lbl_dyk.config(text="")
    lbl_fact.config(text="")
    link_lbl.config(text="")
    link_lbl1.config(text="")


def calculate():  # Tax calculation function
    amount = taxable_income.get()  # Getting data from taxable income entry box
    years = age.get()  # Getting data from age entry box
    if amount <= 0:  # if amount is less or equal to zero, to show error message
        error = "This is not a Taxable Amount."  # error message
        clear_labels()  # To clear all the other labels
        mb.showinfo(title='Error', message=error, icon='warning')  # Displaying error message using message box

    elif years <= 0 and regime.get() == "old":  # if age is less or equal to zero for old regime, to show error message
        error = "You didn't entered a valid age."  # error message
        clear_labels()  # To clear all the other labels
        mb.showinfo(title='Error', message=error, icon='warning')  # Displaying error message using message box

    elif regime.get() != "old" and regime.get() != "new":  # if none of the regime is selected
        error = "You haven't selected any regime."  # error message
        mb.showinfo(title='Error', message=error, icon='warning')  # Displaying error message using message box
        # The above statements are handle input errors

    else:  # if all the inputs are correct, below statements will be executed
        if regime.get() == "old":  # if old regime is selected
            tax = old_tax_calculation(amount, years)  # Passing the data to old tax calculation function
        elif regime.get() == "new":  # if new regime is selected
            tax = new_tax_calculation(amount)  # Passing the data to new tax calculation function
        tax_print = f"₹{int(tax)} "  # Storing the tax in a variable to display
        if amount < 5000000:  # if below 50 lakhs don't need to calculate surcharge
            sur_charge = 0  # the value of surcharge if the amount is less then 50 lakhs
            sur_charge_print = "Not Applicable"  # Display sentence of surcharge if surcharge = 0
            total_tax = f"You owe ₹{int(tax)} in tax."  # Display sentence of total tax if surcharge = 0
        elif amount >= 5000000:
            sur_charge = surcharge(amount, tax)
            sur_charge_print = f"₹{int(sur_charge)}"  # Display sentence of surcharge if surcharge != 0
            total_tax = f"You owe ₹{int(tax) + int(sur_charge)} in tax."  # Display sentence of total tax if surcharge != 0
        exceeding_income = int(amount - (int(tax) + sur_charge))  # Calculating exceeding income after reducing tax from the amount
        exceeding_income_print = f"₹{exceeding_income}"  # Display sentence of exceeding income
        fact_to_display = random_fact()  # storing a random fact in a variable from random_fact function
        lbl1.config(text="Income Tax:", font=("Teko", 14, "bold"), fg="#ff3333")  # Displaying Income tax:
        lbl11.config(text=tax_print, font=("Teko", 14))  # Displaying the tax amount which was calculated above
        lbl2.config(text="Surcharge:", font=("Teko", 14, "bold"), fg="#ff3333")  # Displaying Surcharge:
        lbl22.config(text=sur_charge_print,
                     font=("Teko", 14))  # Displaying the surcharge value which was calculated above
        lbl3.config(text="Total Tax:", font=("Teko", 14, "bold"), fg="#ff3333")  # Displaying Total Tax:
        lbl33.config(text=total_tax, font=("Teko", 14))  # Displaying the total tax amount which was calculated above
        lbl4.config(text="Income Exceeding Tax:", font=("Teko", 14, "bold"),
                    fg="#ff3333")  # Displaying Income Exceeding Tax:
        lbl44.config(text=exceeding_income_print,
                     font=("Teko", 14))  # Displaying the exceeding income value which was calculated above
        lbl_dyk.config(text="Did you know?", font=("Teko", 20, "bold"), fg="green")  # Displaying Did you know?
        lbl_fact.config(text=fact_to_display, font=("Teko", 16),
                        fg="#0080ff")  # Displaying the fact which we got from random_fact function
        link_lbl.config(text="To know more about Indian taxes:", font=("Teko", 16, "bold"),
                        fg="#ff3333")  # Displaying To know more about Indian taxes:
        link_lbl1.config(text="www.incometaxindia.gov.in", fg="blue", font=16,
                         cursor="hand")  # To display with binded website link with a hand cursor


def faq():
    faqs()


def my_history():
    history()


def callback(url):  # To open the binded website
    webbrowser.open_new(url)


# Specifying On the screen widgets of tax calculation section

# Taxable income
taxable_income = IntVar()  # Variable for the Taxable income entry box
Label(frame1, text="Taxable Income", font=("Teko", 14)).place(x=60, y=10)  # Label
ent1 = Entry(frame1, textvariable=taxable_income, width=16, font=("Teko", 14)).place(x=175, y=10)  # Entry box

# Age
age = IntVar()  # Variable for the Age entry box
Label(frame1, text="Age*", font=("Teko", 14)).place(x=130, y=40)  # Label
ent2 = Entry(frame1, textvariable=age, width=16, font=("Teko", 14)).place(x=175, y=40)  # Entry box
Label(frame1, text="*Age is compulsory for Old Tax Regime, not required for New Tax Regime", fg="#ff3333",
      font=("Teko", 12, "bold")).place(x=20, y=110)  # To show that age is compulsory for old regime calculation

# Radio buttons for selecting regime
regime = StringVar()  # Variable for the regime radio buttons
rb1 = Radiobutton(root, text="Old Tax Regime", variable=regime, value="old",
                  font=("Teko", 14)).place(x=60, y=75)  # Old Tax Regime radio button
rb2 = Radiobutton(root, text="New Tax Regime", variable=regime, value="new",
                  font=("Teko", 14)).place(x=230, y=75)  # New Tax Regime radio button

# Button for calculating taxes
Button(frame1, text="Calculate tax", height=1, width=10, font=("Teko", 13, "bold"), fg="#33cc33",
       command=calculate).place(x=150, y=135)  # Button for calling calculate function

# Labels for displaying contents of calculation, fact and error if any
lbl1 = Label(frame1)  # Label for inserting data after calculation of tax
lbl1.place(x=10, y=170)  # Placing the above specified label in proper position

lbl11 = Label(frame1)  # Label for inserting data after calculation of tax
lbl11.place(x=98, y=170)  # Placing the above specified label in proper position

lbl2 = Label(frame1)  # Label for inserting data after calculation of tax
lbl2.place(x=10, y=200)  # Placing the above specified label in proper position

lbl22 = Label(frame1)  # Label for inserting data after calculation of tax
lbl22.place(x=92, y=200)  # Placing the above specified label in proper position

lbl3 = Label(frame1)  # Label for inserting data after calculation of tax
lbl3.place(x=10, y=230)  # Placing the above specified label in proper position

lbl33 = Label(frame1)  # Label for inserting data after calculation of tax
lbl33.place(x=83, y=230)  # Placing the above specified label in proper position

lbl4 = Label(frame1)  # Label for inserting data after calculation of tax
lbl4.place(x=10, y=260)  # Placing the above specified label in proper position

lbl44 = Label(frame1)  # Label for inserting data after calculation of tax
lbl44.place(x=173, y=260)  # Placing the above specified label in proper position

lbl_dyk = Label(frame1)  # Label for displaying Did you know
lbl_dyk.place(x=10, y=300)  # Placing the above specified label in proper position

lbl_fact = Label(frame1, wraplength=480, justify="left")  # Label for little long facts. so, specified wrap and justify
lbl_fact.place(x=10, y=330)  # Placing the above specified label in proper position

link_lbl = Label(frame1)  # Label for displaying To know more about Indian taxes:
link_lbl.place(x=10, y=480)  # Placing the above specified label in proper position

link_lbl1 = Label(frame1)  # Label for displaying the website binded text
link_lbl1.place(x=275, y=480)  # Placing the above specified label in proper position
link_lbl1.bind("<Button>", lambda e: callback("https://tinyurl.com/ju8ha3hn"))  # To bind the website on the text in this label

Button(frame1, text="FAQ's?", height=1, width=5, font=("Teko", 13, "bold"),
       command=faq).place(x=410, y=510)  # Button for calling calculate function

Button(frame1, text="My History", height=1, width=7, font=("Teko", 13, "bold"),
       command=my_history).place(x=10, y=510)  # Button for calling calculate function

# Tax calculation section ends here....

# Calling Mainloop()
root.mainloop()
