# Password generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy version from me
# password = ""

# for L in range(1, nr_letters + 1):
#     random_letters = random.randint(0, 51)
#     password_letters = letters[random_letters]
#     password += password_letters
    
# for S in range(1, nr_symbols + 1):
#     random_symbols = random.randint(0, 8)
#     password_symbols = symbols[random_symbols]
#     print(password_symbols)
#     password += password_symbols
    
# for N in range(1, nr_numbers + 1):
#     random_numbers = random.randint(0, 9)
#     password_numbers = numbers[random_numbers]
#     print(password_numbers)
#     password += password_numbers
    
# print(password) 

# Easy from my teacher

# password = ""

# for L in range(1, nr_letters + 1):
#     random.letters = random.choice(letters)
#     password += random.letters
    
# for S in range(1, nr_symbols + 1):
#     random.symbols = random.choice(symbols)
#     password += random.symbols

# for N in range(1, nr_numbers + 1):
#     random.numbers = random.choice(numbers)
#     password += random.numbers

# print(password)

# Hard version from me

# Mix = nr_letters + nr_symbols + nr_numbers
# password = ""

# for R in range(1, Mix + 1):
#     if R == 1:
#         random_letters = random.randint(0, 51)
#         password_letters = letters[random_letters]
#         password += password_letters
#     elif R == 2:
#         random_symbols = random.randint(0, 8)
#         password_symbols = symbols[random_symbols]
#         print(password_symbols)
#         password += password_symbols
#     else:
#         random_numbers = random.randint(0, 9)
#         password_numbers = numbers[random_numbers]
#         print(password_numbers)
#         password += password_numbers

# print(password)


# Hard version from my teacher

# password= []

# for L in range(1, nr_letters + 1):
#     random.letters = random.choice(letters)
#     password+= random.letters
    
# for S in range(1, nr_symbols + 1):
#     random.symbols = random.choice(symbols)
#     password+= random.symbols

# for N in range(1, nr_numbers + 1):
#     random.numbers = random.choice(numbers)
#     password+= random.numbers

# random.shuffle(password_list)
# password = ""

# for R in password_list:
#     password += R

# print(password)

