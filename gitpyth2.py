import smtplib
from datetime import datetime
my_email = "vython2020@gmail.com"
password = "optionchain"
with open('/home/varun/Documents/projects/mobile/ip.txt','r') as ip:
    #text = ip.read()
    text = "the github/bash/python loop is complete from myhome. jai guru dev"
    print(text, type(text))
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
from_addr=my_email,to_addrs="x16varunk@iima.ac.in",msg="Subject:Ip address\n\n"+str(datetime.now())+"\n"+text)
    connection.close()
