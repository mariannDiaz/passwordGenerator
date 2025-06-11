from password_generator import password_generator, generate_memorable_password, get_words_from_CSV

# This variables are the building blocks for our passwords
uppercare_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*()-_=+~/\\[]{.}?,:;"

def main():
    """

    Main function to run the epassword generator application.
    This function handles all user interaction.

    """

    print("\nWelcome to The Password Generator!\n")

    is_running = True

    """
    You always want to write your while loops with a condition that is 'True'.
    Make that condition 'False' later in the code.
    
    """
    while is_running:
        try:
            # Get user input!
            lenght = input("Insert the character lenght or press Enter for a memorable-password: ")

            # ----------------------- Call the selected Expert Function ---------------------------#

            # This is the way to check if the user just pressed Enter.
            # It explicitly checks if the string is empty.
            # "If the user did not type anything and just pressed Enter, then..."*
            if lenght == "":
                #---------------------- Generate & print the memorable password(s) -------------------------#

                amount = int(input("Insert the amount of passwords you want to generate: "))
                words = get_words_from_CSV("random_words.csv")
                generate_memorable_password(words, amount)

                if input("Do you want to exit this program (y/n): ").lower() == 'y':
                    print("\nThank you for using The Password Generator!\nBye.")
                    is_running = False

            else:
                # User wants a random password
                lenght = int(lenght)
                if lenght <= 0:
                    print("The lenght must be a positive number.")
                    """
                    
                    In a loop, the 'continue' keyword means: "Stop what you're doing in this current run of the loop, 
                    skip everything else below me, and jump immediately back to the top of the loop to start the next run."

                    """
                    # It's a way to bail out of a single, invalid attempt and start fresh without exiting the whole program
                    continue

                amount = int(input("Insert the amount of passwords you want to generate: "))

                #------------------- Build the Character Set for the random password -------------------#
                character_set = ""

                if input("Do you want to include uppercase letters? (y/n): ").lower() == 'y':
                    character_set += uppercare_letters
                if input("Do you want to include lowercase letters? (y/n): ").lower() == 'y':
                    character_set += lowercase_letters
                if input("Do you want to include numbers? (y/n): ").lower() == 'y':
                    character_set += digits
                if input("Do you want to include symbols? (y/n): ").lower() == 'y':
                    character_set += symbols

                # This if statement checks if the character_set string is still empty.    
                if character_set == "":
                    print("\nError: You must select at least one charater type.\nPlease, try again.\n")
                    """ 
                    'continue' jumps right back to the top of the loop,
                    where it will once again ask the user to input a password length.

                    It's a way to bail out of a single, invalid attempt and start fresh without exiting the whole program.

                    """
                    continue

                #------------------------- Generate & print the random password(s) ----------------------------#

                password_generator(amount, lenght, character_set)

                if input("Do you want to exit this program (y/n): ").lower() == 'y':
                    print("\nThank you for using The Password Generator!\nBye.")
                    is_running = False
            
        except ValueError:
            print("\nError. Invalid input. Please enter a number for lenght and amount.\n")
        except Exception as e:
            print(f"\nAn unexpected error has occurred: {e}\n")


# This ensures the main() function is called only when you run this script.
if __name__ == "__main__":

    main()

