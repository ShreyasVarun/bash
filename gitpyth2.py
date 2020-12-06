import smtplib
from datetime import datetime
def send_email(text):
    my_email = "vython2020@gmail.com"
    password = "optionchain"
    #with open('/home/varun/Documents/projects/mobile/ip.txt','r') as ip:
        #text = ip.read()
    #text = "automation done by single .sh file that will update the repo and run this python file. From myhome@ 29-nov-2020,11:05 am   jai guru dev. "
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
    from_addr=my_email,to_addrs="x16varunk@iima.ac.in",msg="Subject:automation update\n\n" + "this mail was sent at " + str(datetime.now())+"\n"+text)
    connection.close()
text = f"single .sh file, send_email function, From continental@ 29-nov-2020,21:12 am   jai guru dev. "
send_email(text)

    
