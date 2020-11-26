import smtplib
from datetime import datetime
my_email = "vython2020@gmail.com"
password = "optionchain"
#with open('/home/varun/Documents/projects/mobile/ip.txt','r') as ip:
    #text = ip.read()
text = "automated 1) the updating of this repo,  and 2)running this python file. done from  myhome/aig. jai guru dev. "
try:
    import tensorflow as tf
    text += str(tf.__version__)
except Exception as e:
    text += str(e)
#print(text, type(text))
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(
from_addr=my_email,to_addrs="x16varunk@iima.ac.in",msg="Subject:automation update\n\n"+str(datetime.now())+"\n"+text)
connection.close()
