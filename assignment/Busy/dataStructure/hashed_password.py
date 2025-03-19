from typing import re

import bcrypt

USER_DETAILS = 'user_details.txt'

username = input("input your username")
password = input("Input your password")
eMail = input("Input your email")


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_to_file(username,hashed_password):
    with open(USER_DETAILS,'a') as file:
        file.write(f'{username}:{hashed_password.decode('utf-8')}\n')
        
def save_to_file(email,hashed_password):
    with open(USER_DETAILS,'a') as file:
        file.write(f'{email}:{hashed_password.decode('utf-8')}\n')

def register_user():
    while True:
        username = input("Input your username")
        if not username:
            print("username cannot be empty")
            continue
        break
    while True:
        password = input("Input your password:")
        if not password:
            print("password cannot be empty")
            continue
        break
    while True:
        email = input("Input your eMail:")
        if not email:
            print("eMail cannot be empty")
            continue
        break
    save_to_file(username,email,hash_password(password))


def validate_user():
    try:
        with open(USER_DETAILS,'r') as file:
            for line in file:
                stored_email,stored_username, stored_password = line.strip().spilt(':')
            if username == stored_username:
                return bcrypt.checkpw(password.encode('utf-8'),stored_password.encode('utf-8'))
            if email == stored_email:
                return bcrypt.checkpw(password.encode('utf-8'),stored_password.encode('utf-8'))
    except FileNotFoundError as e:
        print("File not found", e.filename)
    except ValueError:
        print("Invalid username or password")

    finally:
        print("Thank you for registering")
# with self.assertRaises(InvalidPhoneNumberError) Customer(name: asa, "09091234578")

def login_user():
    username = input("input your username ")
    password = input("enter your password ")
    eMail = input("enter your email ")

    if validate_user(username,password,eMail):
        print("logged in succesfully..")
    else:
        print("Invalid username or password or email")


def exit():
    print("Thank you")
    exit()

def main():
    menu = """
        1 to register user
        2 to login user
        3 to exit
    """ 
    choice = input (menu)

    match choice:

        case "1": register_user()
        case "2": login_user()
        case "3": exit()

password = input("Input your password")
while not re.fullmatch(r'\w{8}',password):
   password = input("Input your password")

main()