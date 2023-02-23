# Password Generator

# Pseudo Code

# -Generate a password with a minimum length
# -Allow user to determine if they want special characters or numbers

# Import modules

import random
import string

# Start

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # create string holding characters
    characters = letters
    if numbers:
        characters += digits
    if special_characters: 
        characters += special

    # create holder for password
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    # Start password generation
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special  

    return pwd       

# user input of password requirements 
min_length = int(input("Enter the minimum password length."))
has_number = input("Do you want to has a number in your password? (y/n)").lower() == "y"
has_special = input("Do you want to has a special character(s) in your password? (y/n)").lower() == "y"

pwd = generate_password(min_length, has_number, has_special)
print("The generated password is : ", pwd)