"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Christian Tamayo
Student ID: ctamayo
File created: October 8, 2024
******************************
This file is used to generate a random password with a given length.
This is done by choosing a random character from a string containing
all possible characters, and concatenating it to the generated
password.
"""

import random

#all characters
ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*/?-+=,.|~"

#generate password
def generate_password(length):
    password = ""

    #concetanate each random character to the string
    for i in range(length):
        password += random.choice(ALL_CHARS)

    return password
