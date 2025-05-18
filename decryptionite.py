#!/usr/bin/env python

import os
from cryptography.fernet import Fernet

files = []

# variable for important decryption requests
sorcerer_letter = "TheSorcererLetter"

for file in os.listdir():
    if file == "curse.py" or file == "thekey.key" or file == "decryptionite.py" or file == sorcerer_letter:
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

# read in the key to a 'secretkey' var
with open("thekey.key", "rb") as key:
    secretkey = key.read()

# iterates through the files and decrypts with the generated key
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()

    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

print("\nthe sorcerer has lifted the curse and restored your files.\n" \
"never return to the land of vazkaban")