import random

def password_generator(amount, length, all):
    for x in range(amount):
        password = "".join(list(random.choices(all, k=length)))
        print(password, "\n")


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