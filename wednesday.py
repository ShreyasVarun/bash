'jai guru dev'
from gitpyth2 import send_email
from datetime import datetime


def main():
     text2 = f'/n latest update is that, i m typing this mail from bhaskar\
          on {datetime.now()}  '
     send_email(text2)
if __name__ == '__main__':
     pass
     

