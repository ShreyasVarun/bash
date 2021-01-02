'jai guru dev'
from datetime import datetime
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
    
def rntn_text():
    return "this is random text generatedby rntn"

def main():
    with open('/home/varun/reports_weekday.txt', 'r') as outfile:
        text2 = outfile.read()
    text2 += '\nthis mail is from saturday file. \nname==main, \nemail is all set'
    send_email(text2)
    

if __name__ == '__main__':
    main()
