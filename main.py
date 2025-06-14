from password_generator import *

# --- Character Sets (Constants) ---
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+~/\\[]{.}?,:;"


def main():
    """
    Main function to run the password generator application.
    This function handles all user interaction.
    """
    print("\nWelcome to The Password Generator!")

    is_running = True
    while is_running:
        try:
            # --- Get User Input ---
            print("\n-------------------------- Menu ----------------------------")
            print("0. To exit.")
            print("1. Generate a random password")
            print("2. Generate a memorable passphrase (from random words)")
            print("3. Generate a password from a sentence (Schneier's scheme)")
            print("------------------------------------------------------------")
            
            choice = input("Choose an option: ")

            if choice == '1':
                # ----------- User wants a random password ------------- #
                length = int(input("\nInsert the character length: "))
                if length <= 0:
                    print("Length must be a positive number.")
                    continue
                
                amount = int(input("Insert the amount of passwords you want to generate: "))
                
                # ----- Build the Character Set for the random password ----- #
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

            elif choice == '2':
                # ------------------ User wants a memorable passphrase ------------------ #
                amount = int(input("\nInsert the amount of passphrases you want to generate: "))
                words = get_words_from_CSV('random_words.csv')
                generate_memorable_password(words, amount)

            elif choice == '3':
                # -------------- User wants to use Schneier's scheme ---------------- #
                user_sentence = input("\nEnter a sentence to convert into a password: ")
                if not user_sentence:
                    print("You must enter a sentence.")
                    continue
                schneier_password(user_sentence)

            elif choice == '0':
                break

            else:
                print("\nInvalid option, please try again.")
                continue

        except ValueError:
            print("\nError: Invalid input. Please enter a number for length and amount.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

        # ---------------- Ask to Continue --------------------- #
        another = input("\nGenerate another password? (y/n): ").lower()
        if another != 'y':
            is_running = False

    print("\nThank you for using The Password Generator!\nBye.")


# This ensures the main() function is called only when you run this script.
if __name__ == "__main__":
   main()
