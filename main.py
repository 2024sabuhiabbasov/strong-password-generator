# program that generates a random password with the following requirements:
# 1. 2 uppercase letters from A to Z
# 2. 2 lowercase letters from a to z
# 3. 2 digits from 0 to 9
# 4. 2 punctuation signs such as !, ?, ", # etc.
# The order of these characters in the password is random.
# The program should not generate the same password each time it is run.

import random

uppercase_letters = [chr(i) for i in range(65, 91)]  # chr() returns a string representing a character whose Unicode code point is the integer i. 65-91 is the range of uppercase letters in the ASCII table
lowercase_letters = [chr(i) for i in range(97, 123)]  # chr() returns a string representing a character whose Unicode code point is the integer i. 97-123 is the range of lowercase letters in the ASCII table
digits = [chr(i) for i in range(48, 58)]  # chr() returns a string representing a character whose Unicode code point is the integer i. 48-58 is the range of digits in the ASCII table
special_characters = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]  # chr() returns a string representing a character whose Unicode code point is the integer i. 33-48, 58-65, 91-97, 123-127 is the range of special characters in the ASCII table

uppercaseLetter1 = random.choice(uppercase_letters)  # random.choice() returns a random element from the uppercase_letters list
uppercaseLetter2 = random.choice(uppercase_letters)  # random.choice() returns a random element from the uppercase_letters list
lowercaseLetter1 = random.choice(lowercase_letters)  # random.choice() returns a random element from the lowercase_letters list
lowercaseLetter2 = random.choice(lowercase_letters)  # random.choice() returns a random element from the lowercase_letters list
digit1 = random.choice(digits)  # random.choice() returns a random element from the digits list
digit2 = random.choice(digits)  # random.choice() returns a random element from the digits list
specialCharacter1 = random.choice(special_characters)  # random.choice() returns a random element from the special_characters list
specialCharacter2 = random.choice(special_characters)  # random.choice() returns a random element from the special_characters list

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + specialCharacter1 + specialCharacter2 # concatenates the uppercaseLetter1, uppercaseLetter2, lowercaseLetter1, lowercaseLetter2, digit1, digit2, specialCharacter1, specialCharacter2 variables into the password variable

password = list(password)  # converts the password variable into a list
random.shuffle(password)  # random.shuffle() shuffles the password list
password = ''.join(password)  # ''.join() joins the password list into a string

print(password)  # prints the password variable