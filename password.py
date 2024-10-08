"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Christian Tamayo
Student ID: ctamayo
File created: October 8, 2024
******************************
This file is used to calculate the strength of a given password.
It determines this based on the amount of different character groups
and the length of the password.
"""

#the symbols group
symbols_arr = ['!','@','#','$','%','^','&','*','/','?','-','+','+',',','.','|','~']

#count groups
def count_groups(pwd):
    #booleans for each character group
    lower = False
    upper = False
    number = False
    symbols = False

    #check for at least one instance of the character group
    for x in pwd:
        if x.islower():
            lower = True
        if x.isupper():
            upper = True
        if x.isdigit():
            number = True
        for i in symbols_arr:
            if x == i:
                symbols = True

    #count truth values (true = 1, false = 0)
    return int(lower) + int(upper) + int(number) + int(symbols)

#password strength
def password_strength(pwd):
    #strength value
    strength = 0

    #check for invalid password (no spacing)
    for x in pwd:
        if x.isspace():
            return 0

    #check length
    length = len(pwd)

    if length > 12:
        strength += 3
    elif length > 8:
        strength += 2
    elif length > 4:
        strength += 1

    #check groups
    groups = count_groups(pwd)

    #groups is irrelevant if length is too short
    if groups > 3 and length > 4:
        strength += 2
    elif groups > 1 and length > 4:
        strength +=1

    return strength
