import os
from cryptography.fernet import Fernet
#this is a simple key generated and stored in a file
key = Fernet.generate_key()
# print(key)

with open('key.txt', 'wb') as file:
    file.write(key)

