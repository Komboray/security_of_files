import os
from cryptography.fernet import Fernet

# we are going to get the key from the file it has been stored in
with open('key.txt','rb') as keyRead:
    key = keyRead.read()
# print(key)
print('We have found the key....',f'{key}')

# we want to hide the contents of a sys.txt
f = Fernet(key)
# so we are going to get the contents of the file
with open('sys.txt', 'rb')as sys:
    text = sys.read()
print(f'Hii ndio content ya hiyo file {text}')

# we are going to enc the file contents
mali_fiche = f.encrypt(text)

# we are going to write the contents into a new file
with open('ficha.txt', 'wb')as ficha:
    ficha.write(mali_fiche)

print('File imeencryptiwa....')





