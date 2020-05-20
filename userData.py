"""
    a user database with CSV files.
    it can take input and allow users to log in/log out/register.
"""


# import packages
import csv
from IPython.display import clear_output


def registerUser():
    """
        handle user registration and writing to csv
    """
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("To register, please enter your info:")
        email = input("E mail: ")
        password = input("Password: ")
        password2 = input("Retype password: ")
        clear_output()
        if password == password2:
            writer.writerow([email, password])
            print("You are now registered!")
        else:
            print("Passwords not matching. Try again.")


def loginUser():
    """ 
        ask for user info and return to login or flase
        if incorrect info
    """
    print("To login, please enter your info:")
    email = input("E mail: ")
    password = input("Password: ")
    clear_output()
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("You are now logged in!")
                return True
    print("Not logged in. Try again.")
    return False


# variables for main loop
active = True
loggedIn = False

# main loop
while active:

    if loggedIn:
        print("1. Logout\n2. Quit")
    else:
        print("1. Login \n2. Register \n3. Quit")
    choice = input("What would u like to do? ").lower()
    clear_output()
    if choice == "register" and loggedIn==False:
        registerUser()
    elif choice == "login" and loggedIn == False:
        loggedIn = loginUser()
    elif choice == "quit":
        active = False
        print("Thanks for using our software!")
    elif choice == "logout" and loggedIn == True:
        loggedIn = False
        print("You are now logged out.")
    else:
        print("Sorry, please try again!")





