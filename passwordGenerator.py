import random
import string
length = int(input("Enter the password length: "))
letters = string.ascii_letters  
numbers = string.digits         
symbols = string.punctuation
total_characters = letters + numbers + symbols
password = ' '
for i in range(length):
    password += random.choice(total_characters)
print("Generated password:", password)
