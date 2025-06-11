import secrets
import csv

def get_words_from_CSV(filename):
    """

    This method opens and reads a CSV file. Then, it returns a list of words using for loops
    Also, it handles potential arrors if the file is not found or is empty.

    """
    try:
        # open(filename, ...): This is the function that opens the file.
        # mode='r': Opens the file in read-only mode. You can only look at the data, not change it!
        # encoding='utf-8': This specifies the character encoding...
        # ...which is a standard way to ensure text and symbols are read correctly.
        # as infile: The opened file object is temporarily named infile.
        # with ...: This with statement is very useful because it guarantees the file will be automatically closed...
        # ... when the program is done with it, even if errors occur.
        with open(filename, mode='r', encoding= 'utf-8') as infile:
            # open(): It doesn't understand that commas or new lines in your CSV have any special meaning.
            # This is where csv.reader() comes in.
            # Take the raw text stream (infile) and interpret it according to the rules of the CSV format.
            # It knows that commas are used to separate individual values (cells)...
            # ...and that new lines are used to separate records (rows).
            reader = csv.reader(infile)
            # We will use this list to store all the words we find in the file.
            # So you have a complete list of all the words at the end.
            # (CONTAINER) Bowl!
            final_word_list = []
            # Loops through each row in the CSV file.
            for row in reader:
                # Loops through each word in the current row.
                for word in row:
                    # Add th word to ur lust if it's not empty.
                    # Prevents empty entries in our final list.
                    if word:
                        final_word_list.append(word)

            return final_word_list
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.\nPlease make sure it is in the same directory.")
        return[]
    except Exception as e:
        print(f"An error occured while reading the file: {e}")
        return[]
    
    '''
    The reader gives you a list of strings for each row it finds.

    Without csv.reader, you would have to write complex code yourself to first split the file by new lines,
    then split each of those lines by commas. csv.reader handles all of that complexity for you in one clean step.

    reader = csv.reader(infile) means: "Create a helper object that knows how to read the infile,
    and give me the data one row at a time, with each row already neatly split into a list of words."

    '''


def password_generator(amount, lenght, character_set):
    """

    This method generates a specified number of criptographically strong passwords
    from agiven set of characters.

    """
    print(f"\n-----Generating {amount} passwords(s) of length {lenght}-----\n")

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


def generate_memorable_password(word_list, amount):
    """

    This method generates an "easy to remember" password using 3-4 random words and a number.
    
    """
    if not word_list:
        print("Could not generate a memorable password because the word list is empty.")
        # This return statement stops the function and exits
        # Prevents the rest of code form running, this can couse an error if the word_list is empty
        return
    
    print(f"\n-------- Generating {amount} memorable passphrase(s) --------\n")
    for _ in range(amount):
        # Randomly pick one item from the list
        # [3, 4]. This means each passphrase will be made of either 3 or 4 words.
        num_words = secrets.choice([3,4])
        # This list will store the wrods for the single passphrase being created in this run of the loop.
        chosen_words = []
        # Loop 'num_words' times to build our list of words. 
        for _ in range(num_words):
            # This line securely picks one random word from the full word_list.
            random_word = secrets.choice(word_list)
            # This adds the random_word that was just picked to the end of the chosen_words list.
            chosen_words.append(random_word)
        
        random_number = str(secrets.randbelow(10001))

        # Create the passphrase, example: "blue-car-runs-fast-756"
        passphrase = "-".join(chosen_words) + "-" + random_number
        print(passphrase)

    print("\n---------------------------------------------------\n")
    