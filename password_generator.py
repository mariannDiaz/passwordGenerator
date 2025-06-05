import random
import csv

def password_generator(amount, length, all):
    for x in range(amount):
        password = "".join(list(random.choices(all, k=length)))
    return password

# def add_symbols(symbols, all):
#         all += symbols
#         print(all)
# def add_numbers(desition, digits):
#     if desition.lower() == 'yes':
#         numbers = True
#         all = all +  digits
#         #print(all) 
#     elif desition.lower() == 'no':
#         desition = False
#     return desition

# def add_uppercases(desition, uppercase_letters):
#     if desition.lower() == 'yes':
#         uppercase = True
#         all = all + uppercase_letters
#         #print(all) 
#     elif desition.lower() == 'no':
#         desition = False
#     return desition

# def add_lowercases(desition, lowercase_letters):
#     if desition.lower() == 'yes':
#         lowercase = True
#         all = all +  lowercase_letters
#         #print(all) 
#     elif desition.lower() == 'no':
#         desition = False
#     return desition