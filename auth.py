#register - first name, last name, phone number, email, password, confirm password
#login - account number and password
##bank operations
# #reset password
# #phone number update

import random
import json

with open("database.json", "r") as dbs:
    database = json.load(dbs)

def init():

    print('Welcome to ZuriBank')

    have_account = int(input('Do you have an account with us?  1(yes)  2(no) \n'))

    if have_account == 1:
        
        login()
    elif have_account == 2:
        
        register()
    
    print('You selected an invalid option')
    init()

def login():
    print('*************** Login ***************')

    account_number_from_user = input('Enter your account number:\n')
    password = input('Enter your password:\n')

    for user_data in database:
        if user_data["Account number"] == account_number_from_user:
            if user_data["Password"] == password:
                bank_operation(user_data) 
            else:
                print('Invalid password')
                print('================ ========== = ========== ===================')
                forgot_password = int(input('Did you forget your password?  1(yes)  2(no)\n'))
                if forgot_password == 1:
                    reset_password(user_data)
                    pass
                    
                else:
                    login()

                
        print('Invalid account number')
        print('================  ========== = ==========  ===================')
        forgot_account_number = int(input('Did you forget your account number?  1(yes)  2(no)\n'))
        if forgot_account_number == 1:
            retrieve_account_number()

        else:
            login()
                    
                        

    
    
def register():
    new_user = {}
    print('*************** Register ***************')
    print('================  ========== = ==========  ===================')
    first_name = input('What is your first name? \n').title()
    last_name = input('What is your last name? \n').title()
    email = input('What is your email address? \n')
    phone_number = input('What is your phone number?\n')
    set_password = password()
    balance = '0'
    account_number = str(generate_account_number())

    new_user["Account number"] = account_number
    new_user["Account name"] = first_name + " " + last_name
    new_user["Email"] = email
    new_user["Phone number"] = phone_number
    new_user["Password"] = set_password
    new_user["Balance"] = balance

    print('Your account has been created successfully')
    print('================  ========== = ==========  ===================')
    print(f'Your account number is {account_number}.')
    print('================  ========== = ==========  ===================')
    print('Keep your account number safe \n')
    print('================  ========== = ==========  ===================')

    database.append(new_user)

    update_db()

    login()

def bank_operation(user):
    print(f'Welcome {user["Account name"]}')
    print('================  ========== = ==========  ===================')

    selected_option = int(input("What would you like to do? \n (1) Deposit  (2) Withdrawal  (3) Check Balance  (4) Log Complaint   (5) Logout  (6) Exit\n"))

    if selected_option == 1: deposit_operation(user)

    elif selected_option == 2:  withdrawal_option(user)

    elif selected_option == 3:   check_balance(user)

    elif selected_option == 4:     log_complaint()
    
    elif selected_option == 5:      logout()

    elif selected_option == 6:
        print('Thank you for banking with us')
        exit()

    print('Invalid Selection')
    bank_operation(user)

def deposit_operation(user):
    balance = int(user["Balance"])
    debit = int(input('How much would you like to withdraw?\n'))
    balance += debit
    user["Balance"] = str(balance)
    print('================  ========== = ==========  ===================')
    print('Your transaction was successful')
    print('================  ========== = ==========  ===================')

    update_db()
    # asking if the user wants to perform another transaction
    
    another_transaction = int(input('\n Do you want to perform another traansaction?  (1) Yes    (2) No\n'))
    if another_transaction == 1:
        bank_operation(user)
        
    print('Thank you for banking with us')
    exit()


def withdrawal_option(user):
    balance = int(user["Balance"])
    debit = int(input('How much would you like to withdraw?\n'))
    balance -= debit
    user["Balance"] = str(balance)
    print('================  ========== = ==========  ===================')
    print('Your transaction was successful')
    print('================  ========== = ==========  ===================')

    update_db()
    # asking if the user wants to perform another transaction
    another_transaction = int(input('\n Do you want to perform another transaction?  (1) Yes    (2) No\n'))
    if another_transaction == 1:
        bank_operation(user)
    
    print('Thank you for banking with us')
    exit()

def check_balance(user):
    balance = user["Balance"]
    print(f"Your current balance is: ${balance}")

    print('================  ========== = ==========  ===================')

    # asking if the user wants to perform another transaction
    another_transaction = int(input('\n Do you want to perform another transaction?  (1) Yes    (2) No\n'))
    if another_transaction == 1:
        bank_operation(user)

    print('Thank you for banking with us')
    exit()
    
def generate_account_number(): return random.randrange(1111111111, 9999999999)

def password():
    # password_match = False
    # while password_match == False:
    new_password = input('Create password \n')
    confirm_password = input('Confirm Password \n')
    if confirm_password == new_password:
        # password_match == True
        return new_password
    
    print('Passwords don\'t match')
    password()

    

def retrieve_account_number():
    print('Please provide your email and phone number:')
    email = input('email\n')
    phone_number = input('phone number\n')
    for user_data in database:
        if user_data["Email"] == email and user_data["Phone number"] == phone_number:
            name = user_data["Account name"]
            account_number = user_data["Account number"]
            print(f'Hi {name}, your account number is {account_number}')
    
    login()



def reset_password(user):
    account = input('Enter account number\n')
    print('Create new password\n')
    new_password = password()
    user["Password"] = new_password
    print('Your password has been updated')

    update_db()

    login()

def log_complaint(user):
    feedback = input('What issue will you like to report?\n')
    print('Thank you for contacting us.')
    another_transaction = int(input('\n Do you want to perform another traansaction?  (1) Yes    (2) No\n'))
    if another_transaction == 1:
        bank_operation(user)
    exit()

def update_info(user):   print('Update data')

def logout():  login()

def update_db():
    with open("database.json", "w") as dbs:
        json.dump(database, dbs)


##### ACTUAL BANKING SYSTEM #####

init()
# register()
