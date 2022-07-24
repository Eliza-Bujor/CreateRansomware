#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#store the files to a list

files = []      #this creates an empty list that will further be used to store the files


for i in os.listdir():  #this will run through every file that it finds in the os.listdir() (represents the directory)
        if i == "ransomware.py" or i == "key.key" or i == "decrypt.py":         #if the current file is called ransomware.py, then it will pass it and not add it
                continue                        # to the list as we don't want to encript this file
        if os.path.isfile(i):                   #this is a builtin fucntion that determines if the things within the directory are files or not (if yes, append, if not, move forward)
                files.append(i)                 #this command will add the current file to the list


print(files)


with open("key.key", "rb") as decrypt_key:
        secret_key =decrypt_key.read()



# this method will go through each file within the list of files and open each file in read binary method as read_file and save the current file to
# the read_content variable, to which we will be using the read method on the file

# this command will go only through the files that we intend to restore

for j in files:
        with open(j, "rb") as read_file:
                read_content = read_file.read()

# decrypt the files
# this will create a new variable that will store the decrypted data
# Fernet will  reference the key generator that will be used to decrypt the file
# .decrypt will reference the content of the file that we want to decrypt
        decrypted_content = Fernet(secret_key).decrypt(read_content)

# this will write the decrypted version back to the file
        with open(j, "wb") as write_file:
                write_file.write(decrypted_content)



