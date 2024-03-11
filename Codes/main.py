import mysql.connector
from tkinter import *
from tkinter import simpledialog
import tkinter as tk
import string
import random
import json


databasename = "Crypto"
host = 'localhost'
user = 'root'
database_password = '130804'

new_account = False
logged_in = False
transact_state = False
invest_state = False

email_input = ''
password_input = ''
money = 0

BTC_price = 30000
ETH_price = 2000
HDV_price = 420.69


def invest():
    global BTC_price, ETH_price, HDV_price

    def buy_btc():
        print("buy btc")
        amount = simpledialog.askfloat("Input", "Enter the amount", minvalue=0)
        print(amount)
        price = amount * BTC_price
        print(price)

    def buy_eth():
        print("buy eth")
        amount = simpledialog.askfloat("Input", "Enter the amount", minvalue=0)
        print(amount)
        price = amount * ETH_price
        print(price)

    def buy_hdv():
        print("buy hdv")
        amount = simpledialog.askfloat("Input", "Enter the amount", minvalue=0)
        print(amount)
        price = amount * HDV_price
        print(price)

    def sell_btc():
        print("sell btc")
        amount = simpledialog.askfloat("Input", "Enter the amount", minvalue=0)
        print(amount)
        price = amount * BTC_price
        print(price)

    def sell_eth():
        print("sell eth")
        amount = simpledialog.askfloat("Input", "Enter the amount", minvalue=0)
        print(amount)
        price = amount * ETH_price
        print(price)

    def sell_hdv():
        print("sell hdv")
        amount = simpledialog.askfloat("Input", "Enter the amount", minvalue=0)
        print(amount)
        price = amount * HDV_price
        print(price)

    window = Tk()
    window.title("Invest")
    window.geometry("370x352")
    window.configure(bg="#1b2629")
    canvas = Canvas(
        window,
        bg="#1b2629",
        height=352,

        width=370,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"invest_assets/background.png")
    background = canvas.create_image(
        184.5, 167.5,
        image=background_img)

    img0 = PhotoImage(file=f"invest_assets/img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=sell_btc,
        relief="flat")

    b0.place(
        x=238, y=98,
        width=82,
        height=23)

    img1 = PhotoImage(file=f"invest_assets/img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=sell_hdv,
        relief="flat")

    b1.place(
        x=238, y=300,
        width=82,
        height=23)

    img2 = PhotoImage(file=f"invest_assets/img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=sell_eth,
        relief="flat")

    b2.place(
        x=236, y=200,
        width=82,
        height=23)

    img3 = PhotoImage(file=f"invest_assets/img3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=buy_hdv,
        relief="flat")

    b3.place(
        x=236, y=163,
        width=82,
        height=24)

    img4 = PhotoImage(file=f"invest_assets/img4.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=buy_btc,
        relief="flat")

    b4.place(
        x=238, y=65,
        width=82,
        height=23)

    img5 = PhotoImage(file=f"invest_assets/img5.png")
    b5 = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=buy_btc,
        relief="flat")

    b5.place(
        x=238, y=263,
        width=82,
        height=24)

    label1 = Label(
        window,
        text=f"${ETH_price}",
        bg="#D9D9D9",
        fg="black",
        font=("Arial", 16)
    )
    label1.place(x=120, y=185)
    label2 = Label(
        window,
        text=f"${BTC_price}",
        bg="#D9D9D9",
        fg="black",
        font=("Arial", 16)
    )
    label2.place(x=120, y=85)
    label3 = Label(
        window,
        text=f"${HDV_price}",
        bg="#D9D9D9",
        fg="black",
        font=("Arial", 16)
    )
    label3.place(x=120, y=285)

    window.resizable(False, False)
    window.mainloop()


def get_money_by_userid(database_name, user_id):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=database_password,
        database=database_name
    )
    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Query to find the money based on the provided UserId
    find_money_query = """
    SELECT Money FROM Customers WHERE UserId = %s;
    """

    # Executing the query with the provided UserId as a parameter
    cursor.execute(find_money_query, (user_id,))

    # Fetching the result
    result = cursor.fetchone()

    # Closing the connection
    connection.close()

    # If the result is not None and Money is not None, return the money, otherwise return 0
    return result[0] if result and result[0] is not None else 0


def find_userid(database_name, mail):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=database_password,
        database=database_name
    )
    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Assuming the tables already exist, otherwise, you can create them if needed.

    # Query to find the UserId based on the provided email
    find_user_query = """
    SELECT UserId FROM Customers WHERE Email = %s;
    """

    # Executing the query with the provided email as a parameter
    cursor.execute(find_user_query, (mail,))

    # Fetching the results
    result = cursor.fetchone()

    # Closing the connection
    connection.close()

    # If the result is not None, return the UserId, otherwise return None
    return result[0] if result else None


def update_money(database_name, user_id, new_money):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=database_password,
        database=database_name
    )
    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Query to update the money based on the provided UserId
    update_money_query = """
    UPDATE Customers SET Money = %s WHERE UserId = %s;
    """

    # Executing the query with the provided new_money and UserId as parameters
    cursor.execute(update_money_query, (new_money, user_id))

    # Committing the changes to the database
    connection.commit()

    # Closing the connection
    connection.close()


def transact():
    def deposit_btn_clicked():
        global money, logged_in
        print("deposit Button Clicked")
        buffer = int(entry0.get())
        money = money + buffer
        print(money)
        update_money(databasename, find_userid(databasename, email_input), money)
        logged_in = True
        window.destroy()

    def withdraw_btn_clicked():
        global money, logged_in
        print("withdraw Button Clicked")
        buffer = int(entry0.get())
        money = money - buffer
        print(money)
        update_money(databasename, find_userid(databasename, email_input), money)
        logged_in = True
        window.destroy()

    window = Tk()
    window.title("Transact")
    window.geometry("370x352")
    window.configure(bg="#1b2629")
    canvas = Canvas(
        window,
        bg="#1b2629",
        height=352,
        width=370,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    entry0_img = PhotoImage(file=f"transact_assets/img_textBox0.png")
    entry0_bg = canvas.create_image(
        177.0, 153.5,
        image=entry0_img)

    entry0 = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry0.place(
        x=105.0, y=131,
        width=144.0,
        height=43)

    img0 = PhotoImage(file=f"transact_assets/img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=deposit_btn_clicked,
        relief="flat")

    b0.place(
        x=16, y=249,
        width=137,
        height=37)

    img1 = PhotoImage(file=f"transact_assets/img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=withdraw_btn_clicked,
        relief="flat")

    b1.place(
        x=200, y=249,
        width=137,
        height=37)

    background_img = PhotoImage(file=f"transact_assets/background.png")
    background = canvas.create_image(
        184.5, 70.5,
        image=background_img)

    window.resizable(False, False)
    window.mainloop()


def profile():
    global money

    def invest_btn_clicked():
        global invest_state
        print("invest Button Clicked")
        invest_state = True
        window.destroy()

    def portfolio_btn_clicked():
        print("portfolioButton Clicked")

    def transact_btn_clicked():
        global transact_state
        print("transact Button Clicked")
        transact_state = True
        window.destroy()

    window = Tk()
    window.geometry("370x352")
    window.configure(bg="#1b2629")
    window.title("Profile")
    canvas = Canvas(
        window,
        bg="#1b2629",
        height=352,
        width=370,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"profile_assets/background.png")
    background = canvas.create_image(
        138.5, 129.5,
        image=background_img
    )

    img0 = PhotoImage(file=f"profile_assets/img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=transact_btn_clicked,
        relief="flat"
    )
    b0.place(
        x=260, y=290,
        width=91,
        height=29
    )

    img1 = PhotoImage(file=f"profile_assets/img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=invest_btn_clicked,
        relief="flat"
    )
    b1.place(
        x=18, y=290,
        width=91,
        height=29
    )

    img2 = PhotoImage(file=f"profile_assets/img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=portfolio_btn_clicked,
        relief="flat"
    )
    b2.place(
        x=139, y=290,
        width=91,
        height=29
    )

    print(f"userid finder {email_input}")
    user_id = find_userid(databasename, email_input)

    # Adding two lines of text
    label1 = Label(
        window,
        text=f"{user_id}",
        bg="#D9D9D9",
        fg="black",
        font=("Arial", 12)
    )
    label1.place(x=170, y=165)

    money = get_money_by_userid(databasename, find_userid(databasename, email_input))

    label2 = Label(
        window,
        text=f"${money}",
        bg="#D9D9D9",
        fg="black",
        font=("Arial", 12)
    )
    label2.place(x=150, y=210)

    window.resizable(False, False)
    window.mainloop()


def create_account(database_name, FN, LN, mail, psswrd):
    global logged_in
    if new_account:
        # Generate a new user ID
        userid = generate_user_id()
        # Establish database connection
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=database_password,
            database=database_name
        )
        try:
            cursor = conn.cursor()
            # Check if the generated user ID already exists in the database
            while True:
                query = "SELECT UserId FROM customers WHERE UserId = %s"
                cursor.execute(query, (userid,))
                row = cursor.fetchone()
                if row is None:
                    break
                print("Duplicate UserID generated. Regenerating...")
                userid = generate_user_id()

            # Load existing user data from the text file
            try:
                with open('user_data.txt', 'r') as file:
                    users = json.load(file)
            except FileNotFoundError:
                print("user_data.txt File to create account not found.")
                users = {}

            # Check if the email address already exists
            if mail in users:
                print("Email already exists.")
            else:
                # Add the new user to the dictionary
                users[mail] = psswrd

                # Save the updated user data to the text file
                with open('user_data.txt', 'w') as file:
                    json.dump(users, file)
                print("User created successfully!")
                logged_in = True
                #profile()

                # Insert the new user into the database
                insert_query = "INSERT INTO Customers (UserId, Email, FirstName, LastName) VALUES (%s, %s, %s, %s)"
                data = (userid, mail, FN, LN)
                cursor.execute(insert_query, data)
                conn.commit()

        finally:
            # Close the cursor and database connection
            conn.close()


def create_account_screen():
    def create_clicked():
        global email_input
        firstname = entry0.get()
        lastname = entry2.get()
        email = entry1.get()
        email_input = email
        password = entry3.get()

        print("Button Clicked")
        print(f"Firstname: {firstname}")
        print(f"Lastname: {lastname}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        create_account(databasename, firstname, lastname, email, password)
        window.destroy()



    window = Tk()
    window.title("Create Account")
    window.geometry("370x352")
    window.configure(bg = "#1b2629")
    canvas = Canvas(
        window,
        bg = "#1b2629",
        height = 352,
        width = 370,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = "createacc_assets/CA_background.png")
    background = canvas.create_image(
        176.0, 98.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"createacc_assets/CA_img_textBox0.png")
    entry0_bg = canvas.create_image(
        89.5, 146.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry0.place(
        x = 30.0, y = 136,
        width = 119.0,
        height = 19)

    entry1_img = PhotoImage(file = f"createacc_assets/CA_img_textBox1.png")
    entry1_bg = canvas.create_image(
        89.5, 203.5,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry1.place(
        x = 30.0, y = 193,
        width = 119.0,
        height = 19)

    entry2_img = PhotoImage(file = f"createacc_assets/CA_img_textBox2.png")
    entry2_bg = canvas.create_image(
        272.5, 146.5,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry2.place(
        x = 213.0, y = 136,
        width = 119.0,
        height = 19)

    entry3_img = PhotoImage(file = f"createacc_assets/CA_img_textBox3.png")
    entry3_bg = canvas.create_image(
        272.5, 203.5,
        image = entry3_img)

    entry3 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry3.place(
        x = 213.0, y = 193,
        width = 119.0,
        height = 19)

    img0 = PhotoImage(file = f"createacc_assets/CA_img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = create_clicked,
        relief = "flat")

    b0.place(
        x = 105, y = 255,
        width = 151,
        height = 44)

    window.resizable(False, False)
    window.mainloop()


def sign_in(eml, psswrd):
    global logged_in, new_account
    # Load existing user data from the text file
    try:
        with open('user_data.txt', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        print("user_data.txt File to sign in not found.")
        users = {}

    print(f"Email: {eml}, Password: {psswrd}")

    # Check if the username exists and the password matches
    if eml in users and users[eml] == psswrd:
        print("Sign in successful!")
        #profile()
        logged_in = True
    else:
        print("Invalid username or password.")


def login_screen():
    global logged_in

    def btn_clicked():
        global new_account
        print("Create account button")
        new_account = True
        main_window.destroy()

    # Function to handle button click event
    def login_btn_clicked():
        global email_input, password_input
        # Retrieve email and password
        email = email_entry.get()
        email_input = email
        password = password_entry.get()

        # Print the email and password (or do whatever you want with these)
        print(f"Email: {email}, Password: {password}")
        sign_in(email, password)
        if logged_in:
            main_window.destroy()


    # Create main application window
    main_window = Tk()
    main_window.title("Login")
    # Set the size and background color of the window
    main_window.geometry("370x352")
    main_window.configure(bg="#1b2629")

    # Create canvas for graphics
    canvas = Canvas(
        main_window,
        bg="#1b2629",
        height=352,
        width=370,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    # Add background image
    background_img = PhotoImage(file=f"login_assets/background.png")
    background = canvas.create_image(155.0, 108.0, image=background_img)

    # Add email entry field
    email_entry_img = PhotoImage(file=f"login_assets/img_textBox0.png")
    email_entry_bg = canvas.create_image(190.5, 154.0, image=email_entry_img)
    email_entry = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
    email_entry.place(x=109.0, y=141, width=163.0, height=24)

    # Add password entry field
    password_entry_img = PhotoImage(file=f"login_assets/img_textBox1.png")
    password_entry_bg = canvas.create_image(190.5, 226.0, image=password_entry_img)
    password_entry = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
    password_entry.place(x=109.0, y=213, width=163.0, height=24)

    # Add login button
    login_btn_img = PhotoImage(file=f"login_assets/img0.png")
    login_btn = Button(
        image=login_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=login_btn_clicked,
        relief="flat")
    login_btn.place(x=115, y=268, width=151, height=43)

    # Add second button
    second_btn_img = PhotoImage(file=f"login_assets/img1.png")
    second_btn = Button(
        image=second_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")
    second_btn.place(x=134, y=318, width=108, height=22)

    # Make the window's size fixed
    main_window.resizable(False, False)

    # Start the main loop
    main_window.mainloop()


def generate_user_id():
    letters = string.ascii_uppercase
    digits = string.digits

    # Generate a random uppercase letter
    first_letter = random.choice(letters)
    # Generate a random three-digit number
    remaining_digits = ''.join(random.choices(digits, k=3))
    # Combine the letter and digits to form the user ID
    user_id = first_letter + remaining_digits
    return user_id


# login_screen()
# while True:
#     if new_account:
#         create_account_screen()
#     if logged_in:
#         profile()
#     if transact_state:
#         transact()
#     if invest():
#         invest()

invest()

