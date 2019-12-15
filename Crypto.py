#slownik z 10 kryptowalutami  gdzie nazwa to cala np Etherium key to link do odpowiedniej strony
#ma sie wykonywac pozniej dal calego dictionary
#sformatowac odpwiednio wiadomosc mailowa , TO NA KONCU
#dodac funkcje obliczająca srednia cene danej kryptowaluty + ile mozemy kupic danej krypto za 10K dolarów z sredniej ceny
#moze dolozyc portfle z zarowno zwyklymi pieniedzmi jak i kryptowalutami , bedzie obslugiwany z konsoli tutaj pokazywal stan , i go przeliczał zaleznie od zmiany kwoty cnie

import requests
import os
import smtplib
from datetime import date

def send_email(username,password,crypto,high_value,low_value,*args):

    mailBody='Notice values of {} -{}'.format(crypto,date.today())+'\n'+str(high_value)+'\n'+str(high_value)

    message = '''From: Python Crypto Service
    Subject: Change of {} value

    {}
    '''.format('bitcoin', mailBody)
    try:
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(username,password)
        #server.sendmail()
        server.close()
        print('email sended')
    except:
        print("e-mail sending gone WRONG, check fails")

def save_url_file( dir, file,msg,crypto):
    url='https://markets.businessinsider.com/currencies/'+crypto+'-usd'
    print(msg.format(file))

    r = requests.get(url, stream = True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)

def find_high_daily_value(file_paths,word='Daily High',*args):
    with open(file_paths,"r+") as file_with_values:
        lines=file_with_values.read().split("\n")
       # print(len(lines))
        i=0
        for line in lines:
            i+=1
            if word in line:
                high_value=lines[i+2]
                high_value=high_value.replace("\t","").replace(",","")
                high_value=float(high_value)
                return high_value
        file_with_values.close()

def find_low_daily_value(file_paths,word="Daily Low",*args):
    with open(file_paths,"r+") as file_with_values:
        lines=file_with_values.read().split("\n")
       # print(len(lines))
        i=0
        for line in lines:
            i+=1
            if word in line:
                low_value=lines[i+2]
                low_value=low_value.replace("\t","").replace(",","")
                low_value=float(low_value)
                return low_value
        file_with_values.close()
#def read_crypto_values(crypto):
    #with open(path,'r') as crypto_value:

def calculate_value(value,cash):
    sum=int(cash)/value
    return sum

from datetime import date
def notice_changes(dirpath,crypto,high_value,low_value):
    time=date.today()
    with open(dirpath+'\\'+crypto+'.txt','a') as file:
        file.write("Notice values of {} -{}".format(crypto,time))
        file.write('\n')
        file.write(str(high_value))
        file.write('\n')
        file.write(str(low_value))
        file.write('\n')
        file.close()



def daily_crypto_values():
    msg = "Please wait - the file {} will be downloaded"
    dire = r'C:\Users\WIKUS\Desktop\CRYPTO_VALUES'
    file = 'VALUE.txt'
    crypto=['btc','eth','xrp','usdt','bcc']
    for c in crypto:
        save_url_file(dire,'VALUE_'+c+'.txt', msg, c)
        notice_changes(dire, c+'_actual_value'+'.txt', find_high_daily_value(dire+'\\'+'VALUE_'+c+'.txt',"Daily High"), find_low_daily_value(dire+'\\'+'VALUE_'+c+'.txt','Daily Low'))
    

def writtin():
    msg = "Please wait - the file {} will be downloaded"
    dire = r'C:\Users\WIKUS\Desktop\CRYPTO_VALUES'
    crypto = ['btc', 'eth', 'xrp', 'usdt', 'bcc']
    string_out='Today {} values of 5 most famous crypto:\n'.format(date.today())
    string_out+='\n'
    for c in crypto:

        string_out+=c+'\t'+str(find_high_daily_value(dire+'\\'+'VALUE_'+c+'.txt'))
        string_out+='\t'
        string_out+=str(find_low_daily_value(dire+'\\'+'VALUE_'+c+'.txt'))
        string_out+='\n'
    print(string_out)
    return string_out

#daily_crypto_values()
