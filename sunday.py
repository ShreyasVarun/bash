'jai guru dev'
from datetime import datetime
from gitpyth2 import send_email
#from my_trax import create_transformer,tokenize_sent,decode_and_detokenize

def main():
    # model = create_transformer()
    text2 = 'I will marry Sruthi Vellanki in June/July 2021!'
    # translation = decode_and_detokenize(tokenized,model)
    # print(f' this is from THURSDAY ')
    # print(translation)
    text2 += f'two weeks to rl exam and is anything brewing between sruthi & me?'
    send_email(text2)

if __name__ == '__main__':
    main()
    print('none')
