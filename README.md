# The Password Generator 

**Name: Mariann Diaz**

**The new Python tool:**
I used the secrets library to ensure that every selected character in your password is safely managed through encryption/decryption. 

## Main features:
This program can generate customized and safe passwords.

    1. Generates a non-customized random password (let the system choose)
    2. Generates a memorable passphrase (made of random words)
    3. Generates a password from a sentence (Schneier's scheme)

## Other features:

    ▪️ You can choose the length and types of characters you want to include in your desired password.
    ▪️ You can generate multiple passwords at once.


## Main Challenges:

    1. To generate memorable but strong passwords. It is necessary to balance both requirements.
    2. Making this program user-friendly, so the user has better control over the expected results.
    3. To open, read, and correctly export the random words in the CSV file.
    4. To fully understand how to use the secrets.choice() tool inside the context of my program.
    5. To successfully implement Bruce Schneier's Scheme into a beginner-friendly program.


## Debugging & Fixing:

    1. The program failed multiple times because of incorrect indentation, wrong conversion of values, issues with importing classes,
       incorrect management of the CSV File imports, and a lack of understanding of the secrets.choice() and "".join() tools.
       Later, I modified the program to function correctly using print statements and debugging. 

    2. Overall reflection: A password should not be hard to remember or easy to decode.
       This statement can be highly contradictory. I learned to balance both requirements in order to produce safe & memorable passwords.


