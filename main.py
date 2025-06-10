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
            # --------------------------------------------- Get User Input ---------------------------------------#
            length_str = input("Insert the character length (or press Enter for a memorable passphrase): ")
            
            # ------------------------ Call the Correct Expert Function ----------------------#
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

