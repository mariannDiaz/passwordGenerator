# # Main (MANAGER CLASS)

# import secrets
# import csv
# from password_generator import *

# uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

# digits = "0123456789"

# symbols = "!@#$%^&*()-_=+~/\\[]{.}?,:;"

# special_string = ""

# uppercase, lowercase, numbers, symbs = True, True, True, True

# # all = ''

# # print("\nWelcome to The Password Generator!")

# # looping = True

# # while(looping == True):

# #     #^^^^^^^^^^^^^^^^^^^^^^^^ USER INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

# #     length = int(input("\nInsert the character lenght you want: "))

# #     amount = int(input("Insert the amount of passwords you want ot generate: "))

# #     menu_option = int(input("\nChoose an option:\n"
# #                             "1. Get a System-generated password."
# #                             "\n2. Make a customized password."
# #                             "\nInsert your option here: "))

# #     if (menu_option < 1 ) or (menu_option > 2):
# #         print("Invalid option. Try again!")
        
# #     elif menu_option == 1:
# #         all += symbols + digits + lowercase_letters + uppercase_letters
# #         system_generated_password = password_generator(amount, length, all)
# #         looping = False

# #     elif menu_option == 2:
# #         submenu_option = int(input("\nChoose an option:\n"
# #                                    "1. Get a random special word in your password."
# #                                    "\n2. Insert a string to customize your password."
# #                                    "\nInsert your option here: "))
# #         if (submenu_option < 1 ) and (submenu_option > 2):
# #             print("Invalid option. Try again!")
# #             break
# #         elif submenu_option == 1:
# #             csv_file = 'random_words.csv'
# #             # Opening the file and reading it are separate steps in Python
# #             with open(csv_file, mode= 'r') as infile: # Check open() documentation
# #                 reader = csv.reader(infile) # Processes lines in the given csv file
# #                 data = list(reader) # Puts lines of CSV into a list
# #                 data = str(data)
# #                 #all += data #+ symbols + digits + lowercase_letters + uppercase_letters
# #                 system_generated_password = password_generator(amount, length, data)
# #                 looping = False
# #         elif submenu_option == 2:
# #             input_special_str = input("Insert your special string: ")
# #             #sub_string = input_special_str[0:5]

# #             all += symbols + digits + lowercase_letters + uppercase_letters #+ sub_string
# #             system_generated_password = password_generator(amount, length, all)
# #             looping = False

#     # all += symbols
#     # print(password_generator(amount,length,all))


# We now import all the "expert" functions from our generator toolkit file.
from password_generator import password_generator, get_words_from_csv, generate_memorable_password

# --- Character Sets (Constants) ---
# These are the building blocks for our random passwords.
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+~/\\[]{.}?,:;"


def main():
    """a
    Main function to run the password generator application.
    This function handles all user interaction.
    """
    print("\nWelcome to The Password Generator!\n")

    while True:
        try:
            # --- Get User Input ---
            length_str = input("Insert the character length (or press Enter for a memorable passphrase): ")
            
            # --- Call the Correct Expert Function ---
            if not length_str:
                # User wants a memorable passphrase.
                amount = int(input("Insert the amount of passphrases you want to generate: "))
                words = get_words_from_csv('random_words.csv')
                generate_memorable_password(words, amount)
            else:
                # User wants a random password.
                length = int(length_str)
                if length <= 0:
                    print("Length must be a positive number.")
                    continue
                
                amount = int(input("Insert the amount of passwords you want to generate: "))
                
                # --- Build the Character Set for the random password ---
                character_set = ""
                if input("Include uppercase letters? (y/n): ").lower() == 'y':
                    character_set += UPPERCASE_LETTERS
                if input("Include lowercase letters? (y/n): ").lower() == 'y':
                    character_set += LOWERCASE_LETTERS
                if input("Include numbers? (y/n): ").lower() == 'y':
                    character_set += DIGITS
                if input("Include symbols? (y/n): ").lower() == 'y':
                    character_set += SYMBOLS
                
                if not character_set:
                    print("\nError: You must select at least one character type. Please try again.\n")
                    continue
                
                # --- Generate and Print Password ---
                password_generator(amount, length, character_set)

        except ValueError:
            print("\nError: Invalid input. Please enter a number for length and amount.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        # --- Ask to Continue ---
        if input("\nGenerate another password? (y/n): ").lower() != 'y':
            break

    print("\nThank you for using The Password Generator!")


# This ensures the main() function is called only when you run this script.
if __name__ == "__main__":
    main()

