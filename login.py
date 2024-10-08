"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Christian Tamayo
Student ID: ctamayo
File created: October 8, 2024
******************************
This file is serves as the login interface for the user.
The user is prompted with the option to create their own
password or generate a random one. The program will continue
to run if a sufficient password strength is not met.
"""

from password import *
from generate import *

def process_password(min_strength):
    valid_password = False

    #run loop until valid
    while not valid_password:
        password = input("input a password, or input 'X' for a randomly generated password \n")

        if "x" in password.lower():
            #generate random
            password = generate_password(15)
            print("Your password: " + password)
        else:
            print("You entered: " + password)

        print("Your password has a strength of " + str(password_strength(password)))

        if password_strength(password) >= min_strength:
            valid_password = True
            print("Your password is strong enough! Thank you.")
        else:
            print("Your password is not strong enough.\n")
