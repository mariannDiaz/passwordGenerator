# We now import all the "expert" functions from our generator toolkit file.
from password_generator import *

# --- Character Sets (Constants) ---
# These are the building blocks for our random passwords.
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+~/\\[]{.}?,:;"


def main():
    """
    Main function to run the password generator application.
    This function handles all user interaction.
    """
    print("\nWelcome to The Password Generator!\n")

    is_running = True
    while is_running:
        try:
            # --- Get User Input ---
            print("\n--- Main Menu ---")
            print("1. Generate a random password")
            print("2. Generate a memorable passphrase (from random words)")
            print("3. Generate a password from a sentence (Schneier's scheme)")
            
            choice = input("Choose an option: ")

            if choice == '1':
                # User wants a random password.
                length = int(input("Insert the character length: "))
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
                
                if character_set == "":
                    print("\nError: You must select at least one character type. Please try again.\n")
                    continue
                
                password_generator(amount, length, character_set)

                another = input("\nGenerate another password? (y/n): ").lower()
                if another != 'y':
                    is_running = False

            elif choice == '2':
                # User wants a memorable passphrase.
                amount = int(input("Insert the amount of passphrases you want to generate: "))
                words = get_words_from_csv('random_words.csv')
                generate_memorable_password(words, amount)

                another = input("\nGenerate another password? (y/n): ").lower()
                if another != 'y':
                    is_running = False

            elif choice == '3':
                # User wants to use Schneier's scheme.
                user_sentence = input("Enter a sentence to convert into a password: ")
                if not user_sentence:
                    print("You must enter a sentence.")
                    continue
                schneier_password(user_sentence)

                another = input("\nGenerate another password? (y/n): ").lower()
                if another != 'y':
                    is_running = False

            else:
                print("Invalid option, please try again.")


        except ValueError:
            print("\nError: Invalid input. Please enter a number for length and amount.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        # --- Ask to Continue ---
        another = input("\nGenerate another password? (y/n): ").lower()
        if another != 'y':
            is_running = False

    print("\nThank you for using The Password Generator!\nBye.")


# This ensures the main() function is called only when you run this script.
if __name__ == "__main__":
    main()
