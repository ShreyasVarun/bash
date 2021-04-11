'jai guru dev'
from datetime import datetime
from gitpyth2 import send_email
#from my_trax import create_transformer,tokenize_sent,decode_and_detokenize

def main():
    # model = create_transformer()
    #text2 = 'I will marry Sruthi Vellanki in June/July 2021!'
    # translation = decode_and_detokenize(tokenized,model)
    # print(f' this is from THURSDAY ')
    # print(translation)
    text2 = f'{datetime.now()} \n'
    text2 += f'hi akka i am in tarnaka. ridhi laddu. shreya cutie. this message was typed from laptop to test the connection of my home jewel'
    send_email(text2)

if __name__ == '__main__':
    #main()
    print('none')
