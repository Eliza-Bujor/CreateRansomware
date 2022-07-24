<h1>Create Ransomware</h1>

<h2>Description</h2>
Project consists of a simple python script that behaves as a ransmoware program. This has helped in gaining more knowledge in python as well as ransomware, knowing how easy it is to create it as well as how it operates. I have decided to use DigitalOcean, a platform that allows me to create virtual machines that I can easily dispose of after implementing the ransomware on it. The machine that we will be targetting today is Ubuntu 22.04. The reason why I focused on ransomware is because ransomware is one of the most devastating malware that can take down big companies as it is quite the struggle to recover from such attacks.
<br />
<br />
However, it is important to know that the typical ransomware is actually more complex than this project, although the idea was to demonstrate how it works and how easy it is to encrypt files and get them decrypted.
<br />

<h2>Environments Used </h2>

- <b>DigitalOcean</b>
- <b>Python</b>
- <b>Windows 10 command prompt</b>

<h2>Program walk-through:</h2>

<p align="center">
Set up the environmnet: <br/>
  
  - <b>After creating the Ubuntu VM we use ssh root@IP in order to get SSH access to the machine</b>
  - <b>We will be using my windows machine to create the connection</b>

<p align="center">
<img src="https://i.imgur.com/8YQy9Wr.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/nw6Ccvo.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Create files that we can use for attacking: <br/>
  
  - <b>First we will create a directory called files</b>
  - <b>In the files directory we will be creating a few files that can be used later on</b>

<p align="center">
<img src="https://i.imgur.com/yf7cJK9.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Create the ransomware python file: <br/>
  
  - <b>Use the command nano ransomware.py to create the python file</b>
  - <b>The nano command will allow you to add text to the freshly created python file</b>

<p align="center">
<img src="https://i.imgur.com/47nkfpW.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Search for the files and add them to a list: <br/>
  
  - <b>Use the command nano ransomware.py to create the python file</b>
  - <b>The nano command will allow you to add text to the freshly created python file</b>

<p align="center">
<img src="https://i.imgur.com/ocYJ8TV.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/sQL1qot.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Reject the directories from being added to the list: <br/>
  
  - <b>Here we have tested what would happen if we were to add a directory to the files directory</b>
  - <b>As it can be noticed, the directory will be also added to the list, so we have to make sure that our script doesn't allow directories to be added</b>

<p align="center">
<img src="https://i.imgur.com/eLHIN59.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/vrTqxga.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/sN1gEgV.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Encrypt the files: <br/>
  
  - <b>First, we need to add a cryptography library that will allow us to encrypt using Fernet</b>
  - <b>Fernet is a symmetric encryption method which assures that the encrypted message cannot be manipulated nor accessible to unauthorised parties (without the key)</b>
  - <b>Because it uses a key to decript, we have to create a key that will be randomly generated using the Fernet library </b>

<p align="center">
<img src="https://i.imgur.com/DVwVAru.png" height="30%" width="30%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/XIHhClS.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />

  - <b>Now we will store the generated key on a file called key.key and we also have to make sure that we exclude this file from being added to the list as we don't intend to encrypt it further on</b>
  
<p align="center">
<img src="https://i.imgur.com/h5Sqy4w.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/n16SB2Q.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/mSl5zQp.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Encrypting and locking up the files: <br/>
  
  - <b>First, we will open the files that we selected as we want to lock up</b>
  - <b>This step is important as we want to have direct access to the content of the files in order to proceed with the encryption process</b>

<p align="center">
<img src="https://i.imgur.com/ah62Qz7.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
  
  - <b>Using Fernet, we will be encrypting the content within the files</b>
  - <b>After successfully encrypting the content, we have to write it back to the file</b>
  - <b>Because of this, we will execute again a with open function, although this time instead of having read binary method, we will be assigning a write binary method as we actually have to write content back to the files, which is the enctypted version of the file</b>

<p align="center">
<img src="https://i.imgur.com/oRiLjYw.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/ktDfzxy.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Writing the decryption script: <br/>
  
  - <b>First we will copy the ransomware.py and rename it to decrypt.py using the command "cp ransomware.py decrypt.py"</b>
  - <b>Because our purpose now is just to decrypt, we will be deleting the key generator file and the function that will store the generated key into the key.key file</b>
    - <b>Instead, now we will perform a with open operation which will open the key.key file that contains the encryption key and open as a read binary mode as we will refer to it as decrypt_key</b>
    - <b>Then we will set a new variable called secret_key taht will store the encrypted content of the file</b>

<p align="center">
<img src="https://i.imgur.com/Lt076Zg.png" height="30%" width="30%" alt="Disk Sanitization Steps"/>
<br />

    - <b>Those are the things that have been changed and explained the changes within the comment sections</b>

<p align="center">
<img src="https://i.imgur.com/ymJ3jpC.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />

    - <b>Here we can notice that the files have been successfully decrypted</b>

<p align="center">
<img src="https://i.imgur.com/LeLMTKw.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
