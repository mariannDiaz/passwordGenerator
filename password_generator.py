import secrets



def password_generator(amount, length, character_set):
    """
    Generates a specified number of cryptographically strong passwords.
    """
    print(f"--- Generating {amount} password(s) of length {length} ---")

    # This outer loop runs once for each password you want to create.
    for _ in range(amount):
        # 1. Create an empty list to hold the characters of our new password.
        password_characters = []

        # 2. Loop 'length' times (e.g., 12 times for a 12-character password).
        for _ in range(length):
            # 3. Securely pick one character from the set.
            new_character = secrets.choice(character_set)
            # 4. Add that new character to our list.
            password_characters.append(new_character)

        # 5. After the loop is done, join all the characters from the list into a single string.
        password = "".join(password_characters)

        # 6. Print the final password.
        print(password)
    print("---------------------------------------------")









# def password_generator(amount, length, all):
#     for x in range(amount):
#         password = "".join(list(random.choices(all, k=length)))
#         print(password, "\n")


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