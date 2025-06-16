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
                    print("Advice:\nLength must be a positive number.")
                elif length > 25:
                    print("Advice:\nYour password length must be shorter than 25 characters.")
                elif length < 8:
                    print("Advice:\nYour password length must be longer or equal to 8 characters.")
                    continue
                
                amount = int(input("Insert the amount of passwords you want to generate: "))
                if (amount < 1) or (amount > 35):
                    print("Advice:\nYou may create a minumun of 1 password \nor a maximum of 35 passwords at a time.")
                
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
                if (amount < 1) or (amount > 35):
                    print("Advice:\nYou may create a minumun of 1 password \nor a maximum of 35 passwords at a time.")

                words = get_words_from_CSV('random_words.csv')
                generate_memorable_password(words, amount)

            elif choice == '3':
                # -------------- User wants to use Schneier's scheme ---------------- #
                user_sentence = input("\nEnter a sentence to convert into a password: ")
                if not user_sentence.strip():
                    print("Advice: White space does not count as a valid sentence.\nPlease, enter a valid sentence.")
                    continue
                elif len(user_sentence) < 8:
                    print("Advice: Your sentence must be at least 8 characters long.")
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
        print("\n")
        if another == 'n'.lower():
            is_running = False
        elif another == 'y'.lower():
            continue
        else:
            another = input("\nYour input is invalid.\n"
            "Insert y to continue with the program or n to stop.\n" \
            "Generate another password? (y/n): ").lower()
            print("\n")

    print("\nThank you for using The Password Generator!\nBye.")


# This ensures the main() function is called only when you run this script.
if __name__ == "__main__":
   main()
