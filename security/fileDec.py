import os
from cryptography.fernet import Fernet

# we are going to get the key from the file it has been stored in
with open('key.txt','rb') as keyRead:
    key = keyRead.read()
# print(key)
print('We have found the key....',f'{key}')

with open('ficha.txt', 'rb') as fichua:
    mali_fiche = fichua.read()

print(f'Tumepata contents za hiyo folder {mali_fiche}')


d = Fernet(key)
# we are going to dec the file contents
mali_safi = d.decrypt(mali_fiche)

print(f'Ndio hiyo content ya hiyo file {mali_safi}')

