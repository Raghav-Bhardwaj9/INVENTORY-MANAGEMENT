import mysql.connector
import tkinter as tk
import re
from tkinter import *
from PIL import ImageTk
import ttkthemes


# Define function to connect to the MySQL database
def connect_to_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="Raghav_bh8642",
        database="world"
    )
    return mydb



# Define function to add customer record to MySQL database
def add_customer_record_to_database():
    customer_name = customer_name_entry.get()
    if any(char.isdigit() for char in customer_name):
         status_label.config(text="customer name should not contain digits.please try again",fg="red", font=("Arial",16))
         return
    customer_address = customer_address_entry.get()
    phone_number = (phone_number_entry.get())
    item_name = selected_option.get()
    item_price = float(item_price_entry.get())
    
    
    if not re.match("^[0-9]*$", phone_number):
            
            status_label.config(text="Phone number should contain digits only. Please try again.", fg="red", font=("Arial",16))
            return
        
    if len(phone_number) != 10:
            
            status_label.config(text="Phone number should be 10 digits long. Please try again.", fg="red", font=("Arial",16))
            return
 
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    
    sql = "INSERT INTO customer (customer_name, customer_address, phone_number, item_name, item_price) VALUES (%s, %s, %s, %s, %s)"
    val = (customer_name, customer_address, phone_number, item_name, item_price)
    mycursor.execute(sql, val)
    
    mydb.commit()
    
    new_id = mycursor.lastrowid
    status_label.config(text=f"New record added with ID: {new_id}.s", font=("Arial",16))
    
    status_label.config(text=f"{item_name} added to database for {customer_name}.",fg="green", font=("Arial",16))


# Define function to get item price from MySQL database
def get_customer_records_from_database():
    customer_name = customer_name_entry.get()
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    
    sql = "SELECT customer_name, customer_address, phone_number, item_name, item_price FROM customer WHERE customer_name = %s"
    val = (customer_name,)
    mycursor.execute(sql, val)
    
    results = mycursor.fetchall()
    
    large_font = ("arial",16, "bold")
    
    if results:
        indent1 = "    "
        indent2 = " "
        output_text = f"{indent2}Customer: {customer_name}\n"
    else:
        error_message = f"Error: Customer:'{customer_name}' not found in database."
    
    for result in results:
        output_text += f"{indent2}Address: {result[1]}\n{indent2} Phone Number: {result[2]}\n"
        output_text += f"{indent2}Item: {result[3]}\n{indent2} Price: ${result[4]:.2f}\n\n"
    status_label.config(text=output_text, font=("Arial",16))
    status_label.config(text=error_message, font=("Arial",16), fg="red")


# Define function to remove item from MySQL database
def remove_item_from_database():
    customer_name = customer_name_entry.get()
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    
    sql = "SELECT item_name FROM customer WHERE customer_name = %s"
    val = (customer_name,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchone()
    
    if result:
        item_name = result[0]
        
        sql = "DELETE FROM customer WHERE customer_name = %s"
        val = (customer_name,)
        mycursor.execute(sql, val)
        
        mydb.commit()
        
        status_label.config(text=f"{item_name} removed from database for {customer_name}.", fg="green", font=("Arial",16))
    else:
        status_label.config(text=f"No customer found in database for {customer_name}.", fg="red", font=("Arial",16))

# Define function to update phone_number or customer_address    
def update_customer_details():
    customer_name = customer_name_entry.get()
    customer_address= customer_address_entry.get()

    status_label.config(text=f"customer_address attributes for {customer_name} updated in the database.", fg="green", font=("Arial",16))
   
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    
    sql = "UPDATE customer SET customer_address= %s WHERE customer_name = %s"
    val = (customer_address, customer_name)
    mycursor.execute(sql, val)
    mydb.commit()
    
    status_label.config(text=f"customer_address attributes for {customer_name} updated in the database.", fg="green", font=("Arial",16))
    return

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "1234":
        login_label.config(text="Login Successful", fg="green", font=("Arial",16))
        win.destroy()
    else:
        login_label.config(text="Invalid username or password", fg="red", font=("Arial",16))

# Create the main window
win = tk.Tk()
win.title("Login")
win.geometry("2160x2160")
#bg_image = tk.PhotoImage(file="ss.png")

backgroundImage=ImageTk.PhotoImage(file=r'C:\Users\HP\OneDrive\Desktop\project\login image.jpg')
bgLabel=Label(win,image=backgroundImage)
bgLabel.place(x=0,y=0)



heading_label = tk.Label(win, text="LOGIN", font=("Arial", 25, "bold"))
heading_label.grid(column=15,row=0,padx=50,pady=10)

# Create the username label and entry
username_label = tk.Label(win, text="Username:", font=("Arial",16))
username_label.grid(row=9, column=0, padx=10, pady=50)
username_entry = tk.Entry(win, font=("Arial",16))
username_entry.grid(row=9, column=1, padx=10, pady=50)

# Create the password label and entry
password_label = tk.Label(win, text="Password:", font=("Arial",16))
password_label.grid(row=10, column=0, padx=50, pady=50)
password_entry = tk.Entry(win, show="*", font=("Arial",16))
password_entry.grid(row=10, column=1, padx=50, pady=50)

# Create the login button and label
login_button = tk.Button(win, text="Login", command=login, font=("Arial",16))
login_button.grid(row=11, column=0, columnspan=2, padx=50, pady=50)
login_label = tk.Label(win, text="", font=("Arial",16))
login_label.grid(row=12, column=0, columnspan=2, padx=50, pady=50)

# Run the main loop
win.mainloop()



window = tk.Tk()
window.title("Shopping Mall Management System")
window.geometry("2160x2160")

backgroundImage=ImageTk.PhotoImage(file=r'C:\Users\HP\OneDrive\Desktop\project\image.jpg')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

heading_label = tk.Label(window, text="SHOPPING MALL MANAGEMENT SYSTEM", font=("Arial", 25, "bold"))
heading_label.grid(column=15,row=0,padx=50,pady=10)


customer_name_label = tk.Label(window, text="Customer Name:", font=("arial",16))
customer_name_label.grid(column=0, row=4, padx=10, pady=10)

customer_name_entry = tk.Entry(window, font=("arial",16))
customer_name_entry.grid(column=1, row=4, padx=10, pady=10)

customer_address_label = tk.Label(window, text="Customer Address:", font=("arial",16))
customer_address_label.grid(column=0, row=5, padx=10, pady=10)

customer_address_entry = tk.Entry(window, font=("arial",16))
customer_address_entry.grid(column=1, row=5, padx=10, pady=10)

phone_number_label = tk.Label(window, text="Phone Number:", font=("arial",16))
phone_number_label.grid(column=0, row=6, padx=10, pady=10)

phone_number_entry = tk.Entry(window, font=("arial",16))
phone_number_entry.grid(column=1, row=6, padx=10, pady=10)

options = ["laptop", "macbook", "iphone", "LED TV"]

item_name_label = tk.Label(window, text="Item Name:", font=("arial",16))
item_name_label.grid(column=0, row=7, padx=10, pady=10)

selected_option = tk.StringVar()
selected_option.set(options[0])

drop_down_menu = tk.OptionMenu(window, selected_option, *options)
drop_down_menu.grid(column=1, row=7, padx=10, pady=10)

#item_name_entry = tk.Entry(window, font=("arial",16))
#item_name_entry.grid(column=2, row=3, padx=10, pady=10)

item_price_label = tk.Label(window, text="Item Price:",font=("arial",16))
item_price_label.grid(column=0, row=9, padx=10, pady=10)

item_price_entry = tk.Entry(window, font=("arial",16))
item_price_entry.grid(column=1, row=9, padx=10, pady=10)

add_customer_record_button = tk.Button(window, text="Add customer record", command=add_customer_record_to_database, width=30, height=3,bg="cyan")
add_customer_record_button.grid(column=0, row=11, padx=10, pady=10)

get_Report_button = tk.Button(window, text="Get Report", command=get_customer_records_from_database, width=30, height=3,bg="cyan")
get_Report_button.grid(column=1, row=11, padx=10, pady=10)

remove_item_button = tk.Button(window, text="Remove Item", command=remove_item_from_database, width=30, height=3,bg="cyan")
remove_item_button.grid(column=0, row=12, padx=10, pady=10)

update_button = tk.Button(window, text="update", command=update_customer_details, width=30, height=3,bg="cyan")
update_button.grid(column=1, row=12, padx=10, pady=10)

status_label = tk.Label(window, text="")
status_label.grid(column=0, row=16, columnspan=2, padx=10, pady=10)

price_label = tk.Label(window, text="")
price_label.grid(column=0, row=17, columnspan=2, padx=10, pady=10)




window.mainloop()