# Main (MANAGER CLASS)

import random
import csv
from password_generator import *

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

digits = "0123456789"

symbols = "!@#$%^&*()-_=+~/\\[]{.}?,:;"

special_string = ""

uppercase, lowercase, numbers, symbs = True, True, True, True

all = ''

menu_option = 0

print("\nWelcome to The Password Generator!\n")

looping = True

while(looping == True):

    #^^^^^^^^^^^^^^^^^^^^^^^^ USER INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

    length = int(input("Insert the character lenght you want: "))

    amount = int(input("Insert the amount of passwords you want ot generate: "))

    menu_option = int(input("Choose an option:\n"
                            "1. Get a System-generated password",
                            "2. Make a customized password"
                            "\nInsert your option here: "))

    if menu_option != 1 or 2:
        print("Invalid option. Try again!")
        break
    elif menu_option == 1:
        all += symbols + digits + lowercase_letters + uppercase_letters
        system_generated_password = password_generator(amount, length, all)
    #elif menu_option == 2:
























    # all += symbols
    # print(password_generator(amount,length,all))
