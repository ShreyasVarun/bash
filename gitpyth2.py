import numpy
import smtplib
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def send_email(msg_body):
    my_email = "vython2020@gmail.com"
    password = "optionchain"   
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
    from_addr=my_email,to_addrs="x16varunk@iima.ac.in",msg="Subject:automation update\n\n" + "this mail was sent at " + str(datetime.now())+"\n"+msg_body)
    connection.close()
    
text2 = f"jai guru dev\npull is working.\nsh file is working\ncrontab is working. 12-dec-2020 9:45 @mhj\n "
reqs = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup2 = BeautifulSoup(reqs.text,"html.parser")
text2 += soup2.find_all("h3")[numpy.random.randint(1,100)].text
send_email(text2)

    
