import secrets
import csv

def password_generator(amount, length, character_set):
    """
    Generates a specified number of cryptographically strong passwords
    from a given set of characters. This version uses a traditional for loop for clarity.
    """
    print(f"--- Generating {amount} password(s) of length {length} ---")

    # This outer loop runs once for each password you want to create.
    for _ in range(amount):
        password_characters = []
        # Loop 'length' times (e.g., 12 times for a 12-character password).
        for _ in range(length):
            # Securely pick one character from the set and add it to our list.
            new_character = secrets.choice(character_set)
            password_characters.append(new_character)

        # Join all the characters from the list into a single string.
        password = "".join(password_characters)
        print(password)

    print("---------------------------------------------")


def get_words_from_csv(filename):
    """
    Reads a CSV file and returns a clean list of words using traditional loops.
    Handles potential errors if the file is not found.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            final_word_list = []
            # Loop through each row in the CSV file.
            for row in reader:
                # Loop through each word in the current row.
                for word in row:
                    # Add the word to our list if it's not empty.
                    if word:
                        final_word_list.append(word)
            return final_word_list

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please make sure it's in the same directory.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []


def generate_memorable_password(word_list, amount):
    """
    Generates an "easy to remember" password using 3-4 random words and a number.
    This version uses a traditional for loop.
    """
    if not word_list:
        print("Could not generate a memorable password because the word list is empty.")
        return

    print(f"--- Generating {amount} memorable passphrase(s) ---")
    for _ in range(amount):
        num_words = secrets.choice([3, 4])
        chosen_words = []
        # Loop 'num_words' times to build our list of words.
        for _ in range(num_words):
            random_word = secrets.choice(word_list)
            chosen_words.append(random_word)
        
        # Add a random number for extra security.
        random_number = str(secrets.randbelow(1000))
        
        # Create the passphrase, e.g., "blue-car-runs-fast-734"
        passphrase = "-".join(chosen_words) + "-" + random_number
        print(passphrase)
    print("-------------------------------------------------")
