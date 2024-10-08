import random

#all characters
ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*/?-+=,.|~"

def generate_password(length):
    password = ""

    #concetanate each random character to the string
    for i in range(length):
        password += random.choice(ALL_CHARS)

    return password

print(generate_password(10))