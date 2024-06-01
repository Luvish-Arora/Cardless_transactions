from tkinter import *
from tkinter import messagebox
import mysql.connector

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "cardless_transactions"
}

# Function to establish database connection
def connect_to_database():
    try:
        db_connection = mysql.connector.connect(**db_config)
        return db_connection
    except mysql.connector.Error as error:
        messagebox.showerror("Database Error", f"Error connecting to the database: {error}")
        return None
a=0
# Function to authenticate account holder login
def authenticate_login():
    account_number = account_number_entry.get()
    pin = pin_entry.get()
    global a
    a=account_number

    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()

        # Placeholder query to check account holder credentials
        query = "SELECT * FROM login WHERE account_number = %s AND pin = %s"
        cursor.execute(query, (account_number, pin))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Successful", "Welcome, Account Holder!")
            open_account_holder_window()
        else:
            messagebox.showerror("Login Failed", "Invalid account number or PIN")

        cursor.close()
        db_connection.close()
        return account_number

# Function to open a new window for account holder actions
def open_account_holder_window():
    # Remove all widgets from the main window
    clear_main_screen()

    # Create account holder dashboard
    welcome_label = Label(root, text="Successful Login\nAccount Holder Dashboard", font=("Arial", 20), fg="white",
                          bg="#34495e")
    welcome_label.pack(pady=20)

    # Buttons for account holder actions
    personal_details_button = Button(root, text="Personal Details", command=personal_details, font=("Arial", 14),
                                     bg="#3498db", fg="white", padx=10, pady=5, bd=2)
    account_details_button = Button(root, text="Account Details", command=account_details, font=("Arial", 14),
                                    bg="#3498db", fg="white", padx=10, pady=5, bd=2)
    loan_status_button = Button(root, text="Loan Status", command=loan_status, font=("Arial", 14), bg="#3498db",
                                fg="white", padx=10, pady=5, bd=2)
    transfer_history_button = Button(root, text="Transfer History", command=transfer_history, font=("Arial", 14),
                                     bg="#3498db", fg="white", padx=10, pady=5, bd=2)
    investment_button = Button(root, text="Investment", command=investment, font=("Arial", 14), bg="#3498db",
                               fg="white", padx=10, pady=5, bd=2)
    credit_score_button = Button(root, text="Credit Score", command=credit_score, font=("Arial", 14), bg="#3498db",
                                 fg="white", padx=10, pady=5, bd=2)
    logout_button = Button(root, text="Logout", command=show_main_screen, font=("Arial", 14), bg="#c0392b", fg="white",
                           padx=10, pady=5, bd=2)

    personal_details_button.pack(pady=10)
    account_details_button.pack(pady=10)
    loan_status_button.pack(pady=10)
    transfer_history_button.pack(pady=10)
    investment_button.pack(pady=10)
    credit_score_button.pack(pady=10)
    logout_button.pack(pady=20)
# Placeholder functions for different actions
def personal_details():
    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()
        global a

        # Fetch personal details based on account_number
        query = "SELECT * FROM personal_details WHERE account_number = %s"
        cursor.execute(query, (a,))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Personal Details", f"Account Number: {result[0]}\n"
                                                     f"First Name: {result[1]}\n"
                                                     f"Last Name: {result[2]}\n"
                                                     f"Account Type: {result[3]}\n"
                                                     f"Address: {result[4]}\n"
                                                     f"Monthly Income: {result[5]}\n"
                                                     f"Email: {result[6]}\n"
                                                     f"Mobile Number: {result[7]}")
        else:
            messagebox.showerror("Error", "Personal details not found.")

        cursor.close()
        db_connection.close()


def account_details():
    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()
        global a

        # Fetch account details based on account_number
        query = "SELECT * FROM account WHERE account_number = %s"
        cursor.execute(query, (a,))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Account Details", f"Account Number: {result[0]}\n"
                                                    f"Balance: {result[1]}\n"
                                                    f"Limit: {result[2]}\n"
                                                    f"Credit Score: {result[3]}\n"
                                                    f"Manager ID: {result[4]}")
        else:
            messagebox.showerror("Error", "Account details not found.")

        cursor.close()
        db_connection.close()


def loan_status():
    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()
        global a
        # Fetch loan details based on account_number
        query = "SELECT * FROM loan WHERE account_number = %s"
        cursor.execute(query, (a,))
        results = cursor.fetchall()

        if results:
            message = "Loan Details:\n"
            for result in results:
                message += f"Loan ID: {result[0]}, Monthly Income: {result[2]}, Loan Amount: {result[3]}, Collateral Description: {result[4]}, Manager ID: {result[5]}\n"
            messagebox.showinfo("Loan Status", message)
        else:
            messagebox.showerror("Error", "No loan details found.")

        cursor.close()
        db_connection.close()


def transfer_history():
    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()
        global a
        # Fetch transfer history based on sender_id or receiver_id
        query = "SELECT * FROM transfer_history WHERE sender_id = %s OR receiver_id = %s"
        cursor.execute(query, (a, a))
        results = cursor.fetchall()

        if results:
            message = "Transfer History:\n"
            for result in results:
                message += f"Transaction ID: {result[0]}, Sender ID: {result[1]}, Receiver ID: {result[2]}, Amount: {result[3]}, Date: {result[4]}, Manager ID: {result[5]}\n"
            messagebox.showinfo("Transfer History", message)
        else:
            messagebox.showerror("Error", "No transfer history found.")

        cursor.close()
        db_connection.close()


def investment():
    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()
        global a
        # Fetch investment details based on account_number
        query = "SELECT * FROM investment WHERE account_number = %s"
        cursor.execute(query, (a,))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Investment Details", f"Investment ID: {result[0]}\n"
                                                       f"Investment Type: {result[2]}\n"
                                                       f"Investment Amount: {result[3]}\n"
                                                       f"Start Date: {result[4]}\n"
                                                       f"End Date: {result[5]}\n"
                                                       f"Manager ID: {result[6]}")
        else:
            messagebox.showerror("Error", "Investment details not found.")

        cursor.close()
        db_connection.close()


def credit_score():
    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()
        global a
        # Fetch credit score details based on account_number
        query = "SELECT * FROM credit_score WHERE account_number = %s"
        cursor.execute(query, (a,))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Credit Score", f"Current Loan ID: {result[1]}\n"
                                                  f"Loan Amount: {result[2]}\n"
                                                  f"Previous Loan Details: {result[3]}\n"
                                                  f"Current Credit Score: {result[4]}\n"
                                                  f"Manager ID: {result[5]}")
        else:
            messagebox.showerror("Error", "Credit score details not found.")

        cursor.close()
        db_connection.close()
def view_account_details():
    # Get manager_id from the login page
    manager_id = manager_id_entry.get()

    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()

        # Fetch account details for the specific manager_id
        query = "SELECT * FROM account WHERE manager_id = %s"
        cursor.execute(query, (manager_id,))
        results = cursor.fetchall()

        if results:
            message = "Account Details:\n"
            for result in results:
                message += f"Account Number: {result[0]}, Balance: {result[1]}, Credit Limit: {result[2]}, Credit Score: {result[3]}\n"
            messagebox.showinfo("Account Details", message)
        else:
            messagebox.showerror("Error", "No account details found for this manager.")

        cursor.close()
        db_connection.close()

def view_loan_details():
    # Get manager_id from the login page
    manager_id = manager_id_entry.get()

    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()

        # Fetch loan details for the specific manager_id
        query = "SELECT * FROM loan WHERE manager_id = %s"
        cursor.execute(query, (manager_id,))
        results = cursor.fetchall()

        if results:
            message = "Loan Details:\n"
            for result in results:
                message += f"Loan ID: {result[0]}, Monthly Income: {result[2]}, Loan Amount: {result[3]}, Collateral Description: {result[4]}\n"
            messagebox.showinfo("Loan Details", message)
        else:
            messagebox.showerror("Error", "No loan details found for this manager.")

        cursor.close()
        db_connection.close()

def view_investment_details():
    # Get manager_id from the login page
    manager_id = manager_id_entry.get()

    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()

        # Fetch investment details for the specific manager_id
        query = "SELECT * FROM investment WHERE manager_id = %s"
        cursor.execute(query, (manager_id,))
        results = cursor.fetchall()

        if results:
            message = "Investment Details:\n"
            for result in results:
                message += f"Investment ID: {result[0]}, Investment Type: {result[2]}, Investment Amount: {result[3]}, Start Date: {result[4]}, End Date: {result[5]}\n"
            messagebox.showinfo("Investment Details", message)
        else:
            messagebox.showerror("Error", "No investment details found for this manager.")

        cursor.close()
        db_connection.close()

def view_manager_branch_details():
    # Get manager_id from the login page
    manager_id = manager_id_entry.get()

    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()

        # Fetch manager branch details for the specific manager_id
        query = "SELECT * FROM manager_branch_details WHERE manager_id = %s"
        cursor.execute(query, (manager_id,))
        results = cursor.fetchall()

        if results:
            message = "Manager Branch Details:\n"
            for result in results:
                message += f"Branch ID: {result[0]}, Branch Name: {result[1]}, Location: {result[2]}, Manager ID: {result[3]}\n"
            messagebox.showinfo("Manager Branch Details", message)
        else:
            messagebox.showerror("Error", "No manager branch details found for this manager.")

        cursor.close()
        db_connection.close()

# Modify show_manager_login_screen function to include new buttons for manager actions
def after_show_manager_login_screen():
    # Hide all other widgets
    hide_all_widgets()

    # Add new buttons for manager actions
    account_details_button = Button(root, text="Account Details", command=view_account_details, font=("Arial", 14),
                                    bg="#3498db", fg="white", padx=10, pady=5, bd=2)
    loan_details_button = Button(root, text="Loan Details", command=view_loan_details, font=("Arial", 14),
                                 bg="#3498db", fg="white", padx=10, pady=5, bd=2)
    investment_details_button = Button(root, text="Investment Details", command=view_investment_details, font=("Arial", 14),
                                       bg="#3498db", fg="white", padx=10, pady=5, bd=2)
    manager_branch_details_button = Button(root, text="Manager Branch Details", command=view_manager_branch_details, font=("Arial", 14),
                                           bg="#3498db", fg="white", padx=10, pady=5, bd=2)
    logout_button = Button(root, text="Logout", command=show_main_screen, font=("Arial", 14), bg="#c0392b", fg="white",
                           padx=10, pady=5, bd=2)

    account_details_button.pack(pady=10)
    loan_details_button.pack(pady=10)
    investment_details_button.pack(pady=10)
    manager_branch_details_button.pack(pady=10)
    logout_button.pack(pady=20)

# Function to authenticate manager login
def authenticate_manager_login():
    manager_id = manager_id_entry.get()
    code = code_entry.get()

    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()

        # Placeholder query to check manager credentials
        query = "SELECT * FROM manager WHERE manager_id = %s AND code = %s"
        cursor.execute(query, (manager_id, code))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Successful", "Welcome, Manager!")
            after_show_manager_login_screen()
            # Code to navigate to manager dashboard or perform actions
        else:
            messagebox.showerror("Login Failed", "Invalid manager ID or code")

        cursor.close()
        db_connection.close()

# Function to insert account details into the database
import random

import random

def insert_account_details():
    # Retrieve entered account details
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    account_type = account_type_entry.get()
    address = address_entry.get()
    monthly_income = float(monthly_income_entry.get())  # Convert to float
    email = email_entry.get()
    mobile_number = mobile_number_entry.get()
    balance = float(balance_label_entry.get())  # Convert to float

    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()

        # Generate a random account number and check uniqueness

        account_number = None
        while True:
            account_number = random.randint(1, 1000)
            # Check if the generated account number is not already in use
            cursor.execute("SELECT * FROM personal_details WHERE account_number = %s", (account_number,))
            if not cursor.fetchone():  # If no existing record found with this account number
                break  # Exit the loop


        # Select a random manager_id from the manager table
        cursor.execute("SELECT manager_id FROM manager")
        manager_ids = [row[0] for row in cursor.fetchall()]
        manager_id = random.choice(manager_ids)

        # Insert data into personal_details table
        insert_personal_query = "INSERT INTO personal_details (account_number, first_name, last_name, account_type, address, monthly_income, email, mobile_number, manager_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        personal_data = (account_number, first_name, last_name, account_type, address, monthly_income, email, mobile_number, manager_id)

        try:
            cursor.execute(insert_personal_query, personal_data)
            db_connection.commit()
            messagebox.showinfo("Success", "Account details submitted successfully!")
        except mysql.connector.Error as error:
            db_connection.rollback()
            messagebox.showerror("Database Error", f"Failed to insert account details: {error}")

        # Calculate credit limit (35% of balance)
        credit_limit = balance * 0.35
        credit_limit = round(credit_limit, 2)

        # Insert data into account table
        credit_score=0

        insert_account_query = "INSERT INTO account (account_number, balance, `limit`, credit_score, manager_id) VALUES (%s, %s, %s, %s, %s)"
        account_data = (account_number, balance, credit_limit, credit_score, manager_id)  # Assuming credit_score is set to 0 initially

        try:
            cursor.execute(insert_account_query, account_data)
            db_connection.commit()
            messagebox.showinfo("Success", "Account details submitted successfully!")
        except mysql.connector.Error as error:
            db_connection.rollback()
            messagebox.showerror("Database Error", f"Failed to insert account details: {error}")

        cursor.close()
        db_connection.close()

# Function to show the main screen with login options
def show_main_screen():
    # Hide all other widgets
    hide_all_widgets()



    # Show main login widgets
    account_number_label.pack()
    account_number_entry.pack()
    pin_label.pack()
    pin_entry.pack()
    login_button.pack(pady=20)
    manager_login_button.pack(pady=10)
    create_account_button.pack(pady=10)
    exit_button.pack(side=LEFT, padx=10, pady=20)


# Function to show the manager login screen
def show_manager_login_screen():
    # Hide all other widgets
    hide_all_widgets()

    # Show manager login widgets
    manager_id_label.pack(pady=10)
    manager_id_entry.pack(pady=10)
    code_label.pack(pady=10)
    code_entry.pack(pady=10)
    global login_manager_button  # Define the button as global
    login_manager_button = Button(root, text="Login", command=authenticate_manager_login, font=("Arial", 14), bg="#3498db", fg="white", padx=10, pady=5, bd=2)
    login_manager_button.pack(pady=10)
    back_button.pack(pady=10)

# Function to hide all widgets
def hide_all_widgets():
    for widget in root.winfo_children():
        widget.pack_forget()
def clear_main_screen():
    for widget in root.winfo_children():
        widget.pack_forget()
# Function to handle "Create Account" button click
def create_account():
    # Hide all other widgets
    hide_all_widgets()
    welcome_label = Label(root, text="Enter the following details", font=("Arial", 20), fg="white", bg="#34495e")
    welcome_label.pack(pady=0.5)

    # Show account creation widgets
    first_name_label.pack(pady=5)
    first_name_entry.pack(pady=5)
    last_name_label.pack(pady=5)
    last_name_entry.pack(pady=5)
    account_type_label.pack(pady=5)
    account_type_entry.pack(pady=5)
    address_label.pack(pady=5)
    address_entry.pack(pady=5)
    monthly_income_label.pack(pady=5)
    monthly_income_entry.pack(pady=5)
    email_label.pack(pady=5)
    email_entry.pack(pady=5)
    mobile_number_label.pack(pady=5)
    mobile_number_entry.pack(pady=5)
    balance_label.pack(pady=5)
    balance_label_entry.pack(pady=5)
    submit_button.pack(pady=20)
    back_button.pack(pady=10)

# Function to handle "Exit" button click
def exit_application():
    if messagebox.askokcancel("Exit Application", "Do you want to exit?"):
        root.destroy()

# Main GUI window
root = Tk()
root.title("Cardless Transactions Management System")
root.geometry("800x600")
root.configure(bg="#34495e")

# Heading Label
heading_label = Label(root, text="Cardless Transactions Management System", font=("Arial", 24), fg="white", bg="#34495e")
heading_label.pack(pady=20)

# Account Number Entry
account_number_label = Label(root, text="Account Number:", font=("Arial", 14), fg="white", bg="#34495e")
account_number_entry = Entry(root, font=("Arial", 14), bd=2)

# PIN Entry
pin_label = Label(root, text="PIN:", font=("Arial", 14), fg="white", bg="#34495e")
pin_entry = Entry(root, show="*", font=("Arial", 14), bd=2)

# Manager Login Entry
manager_id_label = Label(root, text="Manager ID:", font=("Arial", 14), fg="white", bg="#34495e")
manager_id_entry = Entry(root, font=("Arial", 14), bd=2)
code_label = Label(root, text="Code:", font=("Arial", 14), fg="white", bg="#34495e")
code_entry = Entry(root, show="*", font=("Arial", 14), bd=2)

# Create Account Entry
first_name_label = Label(root, text="First Name:", font=("Arial", 14), fg="white", bg="#34495e")
first_name_entry = Entry(root, font=("Arial", 14), bd=2)
last_name_label = Label(root, text="Last Name:", font=("Arial", 14), fg="white", bg="#34495e")
last_name_entry = Entry(root, font=("Arial", 14), bd=2)
account_type_label = Label(root, text="Account Type:", font=("Arial", 14), fg="white", bg="#34495e")
account_type_entry = Entry(root, font=("Arial", 14), bd=2)
address_label = Label(root, text="Address:", font=("Arial", 14), fg="white", bg="#34495e")
address_entry = Entry(root, font=("Arial", 14), bd=2)
monthly_income_label = Label(root, text="Monthly Income:", font=("Arial", 14), fg="white", bg="#34495e")
monthly_income_entry = Entry(root, font=("Arial", 14), bd=2)
email_label = Label(root, text="Email:", font=("Arial", 14), fg="white", bg="#34495e")
email_entry = Entry(root, font=("Arial", 14), bd=2)
mobile_number_label = Label(root, text="Mobile Number:", font=("Arial", 14), fg="white", bg="#34495e")
mobile_number_entry = Entry(root, font=("Arial", 14), bd=2)
balance_label = Label(root, text="Balance:", font=("Arial", 14), fg="white", bg="#34495e")
balance_label_entry = Entry(root, font=("Arial", 14), bd=2)

# Login Button
login_button = Button(root, text="Login", command=authenticate_login, font=("Arial", 14), bg="#3498db", fg="white", padx=10, pady=5, bd=2)

# Manager Login Button
manager_login_button = Button(root, text="Manager Login", command=show_manager_login_screen, font=("Arial", 14), bg="#3498db", fg="white", padx=10, pady=5, bd=2)

# Create Account Button
create_account_button = Button(root, text="Create Account", command=create_account, font=("Arial", 14), bg="#2ecc71", fg="white", padx=10, pady=5, bd=2)

# Submit Button
submit_button = Button(root, text="Submit", command=insert_account_details, font=("Arial", 14), bg="#2ecc71", fg="white", padx=10, pady=5, bd=2)

# Back Button
back_button = Button(root, text="Back", command=show_main_screen, font=("Arial", 14), bg="#c0392b", fg="white", padx=10, pady=5, bd=2)

# Exit Button
exit_button = Button(root, text="Exit", command=exit_application, font=("Arial", 14), bg="#e74c3c", fg="white", padx=10, pady=5, bd=2)

# Show main login widgets initially
show_main_screen()

# Run main window
root.mainloop()
