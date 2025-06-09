import secrets
import csv

def get_words_from_CSV(filename):
    """
    This method opens and reads a CSV file. Then, it returns a list of words using for loops
    Also, it handles potential arrors if the file is not found or is empty.

    """
    try:
        with open(filename, mode='r', encoding= 'utf-8') as infile:
            reader = csv.reader(infile)
            







def password_generator(amount, lenght, character_set):
    """
    This method generates a specified number of criptographically strong passwords
    from agiven set of characters.

    """
    print(f"-----Generating {amount} passwords(s) of length {lenght}-----")

    # This outer loop runs once for each password yo want to create
    for _ in range(amount):
        # Empty box (empty list) will store all the characters for one password at a time
        password_characters = [] 
        # Loops 'length' times (example, 12 times for a 12-character password)
        for _ in range(lenght):
            # secrets.choice() securely picks one random character from the character_set string
            new_character = secrets.choice(character_set)
            password_characters.append(new_character) # and adds it to our list

        # Join all the characters frorm the list into a single string
        password = "".join(password_characters)
        print(password)

    print("\n----------------------------------------------------\n")



