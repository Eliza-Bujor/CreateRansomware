<h1>Create Ransomware</h1>

<h2>Description</h2>
Project consists of a simple python script that behaves as a ransmoware program. This has helped in gaining more knowledge in python as well as ransomware, knowing how easy it is to create it as well as how it operates. The 
<br />

<h2>Environments Used </h2>

- <b>Kali Linux</b>
- <b>Python</b>

<h2>Program walk-through:</h2>

<p align="center">
Launch the VMs and get Nessus ready: <br/>
  
  - <b>2 separate VMs have been prepared and launched (Windows 10 on the left and Kali Linux on the right)</b>
  - <b>On the Kali VM is displayed the installation process of the Nessus Essential after the packet has been downloaded</b>
  - <b>Within the terminator, the process of extracting the file and starting Nessus has been executed</b>
  - <b>After starting Nessus, an URL will be provided, with the help of which we can start a connection via SSL</b>

<p align="center">
<img src="https://i.imgur.com/8npYHOp.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Get the IP address of the Windows' VM:  <br/>
  
  - <b>This command has been executed using ipconfig within the command prompt</b>

<p align="center">
<img src="https://i.imgur.com/66Nmn9P.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the number of passes: <br/>
  
  - <b>Ping the IP address of the Windows' VM from Kali's VM to check if the machine can be reached</b>
  - <b>If the machine couldn't be reached, a request time out will be displayed when ping command was to be executed</b>
  - <b>In the case of this error occuring, the firewall within the Windows' VM could prevent us from establishing the connection, and such, we could disable the firewall, which usually is not recommended for production purposes, however in some canses it could depend</b>
  
<p align="center">
<img src="https://i.imgur.com/kRjkihr.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Disabling firewall:  <br/>
  
  - <b>This is how the firewall could be disabled </b>
  
<p align="center">
<img src="https://i.imgur.com/1w8srUu.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  
  - <b>Select the off option and then press Apply and then Ok </b>
  
<p align="center">
<img src="https://i.imgur.com/S3Xrto3.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Implement host discovery scan:  <br/>
  
  - <b>By implementing a host disocvery scan, we will be searching for open ports within the host</b>
  - <b>This is a great tool to enumerate the systems that are on our network</b>
  
<p align="center">
<img src="https://i.imgur.com/Rk335yo.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  
  - <b>By targetting 10.0.2.0/24, we will be targetting the local network of the Windows machine</b>

<p align="center">
<img src="https://i.imgur.com/5emTEN6.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  
  - <b>This sections displays what is gonna happen after we run the scan, what will be the output ports</b>
  - <b>By selecting the Host enumeration scan type we are choosing to display only the systems that are on the network</b>

<p align="center">
<img src="https://i.imgur.com/pVnOiCR.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Results of the host discovery scan:  <br/>
<img src="https://i.imgur.com/7sqxQzs.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  
  - <b>Because we didn't run a vulnerability test, nothing will be displayed on the vulnerability tab</b>
  
<p align="center">
<img src="https://i.imgur.com/UDoTtUC.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Basic vulnerability scan:  <br/>
  
  - <b>Here we performed a basic vulnerability scan on the IP address of the Windows' VM</b>
  - <b>The scan has been set to be automatically done every day at 2.30pm</b>
  
<p align="center">
<img src="https://i.imgur.com/k8DSizi.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
After running the basic vulnerability scan:  <br/>
  
  - <b>The name of the basic vulnerability scan is Windows 10 Single Host scan and it can be noticed that the last scan has been done at 2:38PM today</b>
  
<p align="center">
<img src="https://i.imgur.com/4wkLzgW.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Results of the scan:  <br/>
<p align="center">
<img src="https://i.imgur.com/ZGLxOFe.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  
  - <b>On the vulnerability section of the scan, it can be noticed that only 1 of the scans is critical and majority of the vulnerabilities are info</b>
  
<p align="center">
<img src="https://i.imgur.com/ukbhbV2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  
  - <b>Here we can deduce that those issues are related to eachother, and usually if we try to solve one of them, the others will be solved as well</b>
  
<p align="center">
<img src="https://i.imgur.com/lwBSxe4.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
<br />
<br />
Enabling credentials:  <br/>
  
  - <b>The Windows VM has been set up to accept authenticated scans</b>
  - <b>Credentials to Nessus have been provided and a rescan will take place</b>
  - <b>First we will enable Remote Registry that will allow the scanner to connect to this computer's registry </b>
  - <b>This will allow Nessus to search for insecure configurations such as deprecated cypher suites for example</b>
  
<p align="center">
<img src="https://i.imgur.com/ZhSmi0K.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
  
  - <b>Next thing will be to check if the file and printer sharing are on as well as network discovery</b>
  
<p align="center">
<img src="https://i.imgur.com/lz3rYV8.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>

  - <b>Disable the notifications when changes are done at the computer, as we will be modifying things on it</b>
  
<p align="center">
<img src="https://i.imgur.com/CeiWFqr.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>

  - <b>In the registry editor we will be adding a key that will furhter disable user account control for the remote account that we will be using to connect to the Windows account during the scan</b>
  - <b>The documentation has been taken from Nessus regarding the credentials</b>
  - <b>Navigate to Local_machine -> Software -> Microsoft ->Windows -> Current version -> Policies -> System, where we will create a DWORD and set its value to 1 and then restart the VM</b>
  
<p align="center">
<img src="https://i.imgur.com/IYBbXby.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Rescanning the Windows VM:  <br/>
  
  - <b>Now we can add Windows credentials to the Scan that we previously created and then run the scan one more time</b>
  
<p align="center">
<img src="https://i.imgur.com/u5yBzD2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
<br />
<br />
Results of the rescan after the implementation of credentials:  <br/>
  
  - <b>Now we can add Windows credentials to the Scan that we previously created and then run the scan one more time</b>
  
<p align="center">
<img src="https://i.imgur.com/3VkqICE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
  
  - <b>As this vulnerability is mostly Microsoft Edge, this issue could be solved by applying Windows updates</b>
  
<p align="center">
<img src="https://i.imgur.com/gbN6jsH.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
<br />
<br />
Installing a deprecated Firefox on Windows VM:  <br/>
  
<p align="center">
<img src="https://i.imgur.com/Q8lZWJj.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
  
  - <b>Now, without doing anything else to the Windows VM we will start rerunning the scan</b>
  
<p align="center">
<img src="https://i.imgur.com/3Ptx7KT.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
<img src="https://i.imgur.com/3Dr0zly.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
  
  - <b>Because this version of the Firefox is so old, it has a lot of vulnerabilities</b>
  - <b>Those vulnerabilities can be remediated by just updating Firefox to the latest version or uninstall it</b>
  
<p align="center">
<img src="https://i.imgur.com/WiS0nDu.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  
  - <b>This is what will be displayed on the remediation tab</b>
  
<p align="center">
<img src="https://i.imgur.com/R8Vbb2A.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
<br />
<br />
Remediate the vulnerabilities:  <br/>
  
  - <b>First we will uninstall the old version Firefox by accessing appwiz.cpl</b>
  
<p align="center">
<img src="https://i.imgur.com/0IABucz.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
  
  - <b>Then, perform Windows updates until we have it up to date</b>
  
<p align="center">
<img src="https://i.imgur.com/ZC9HW6m.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
  
  - <b>Run the scan again and check for vulnerabilities</b>
  
<p align="center">
<img src="https://i.imgur.com/RdxyLAF.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  
  - <b>The remaining vulnerabilities will be around Microsoft Edge, and this could possibly happen because Windows might have not updated Microsoft Edge</b>
  - <b>To solve this issue, we could manualy update Microsoft Edge</b>
  
<p align="center">
<img src="https://i.imgur.com/5sMvz93.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>  
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
