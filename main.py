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

print("\nWelcome to The Password Generator!\n")

looping = True

while(looping == True):

    #^^^^^^^^^^^^^^^^^^^^^^^^ USER INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

    length = int(input("Insert the character lenght you want: "))

    amount = int(input("Insert the amount of passwords you want ot generate: "))

    menu_option = int(input("\nChoose an option:\n"
                            "1. Get a System-generated password."
                            "\n2. Make a customized password."
                            "\nInsert your option here: "))

    if (menu_option < 1 ) and (menu_option > 2):
        print("Invalid option. Try again!")
        break
    elif menu_option == 1:
        all += symbols + digits + lowercase_letters + uppercase_letters
        system_generated_password = password_generator(amount, length, all)
        looping = False

    elif menu_option == 2:
        submenu_option = int(input("\nChoose an option:\n"
                                   "1. Get a random special word in your password."
                                   "\n2. Insert a string to customize your password."
                                   "\nInsert your option here: "))
        if (submenu_option < 1 ) and (submenu_option > 2):
            print("Invalid option. Try again!")
            break
        elif submenu_option == 1:
            csv_file = 'random_words.csv'
            # Opening the file and reading it are separate steps in Python
            with open(csv_file, mode= 'r') as infile: # Check open() documentation
                reader = csv.reader(infile) # Processes lines in the given csv file
                data = list(reader) # Puts lines of CSV into a list
                data = str(data)
                #all += data #+ symbols + digits + lowercase_letters + uppercase_letters
                system_generated_password = password_generator(amount, length, data)
                looping = False
        elif submenu_option == 2:
            input_special_str = input("Insert your special string: ")
            #sub_string = input_special_str[0:5]

            all += symbols + digits + lowercase_letters + uppercase_letters #+ sub_string
            system_generated_password = password_generator(amount, length, all)
            looping = False

























    # all += symbols
    # print(password_generator(amount,length,all))
