#The Advanced Port Scanner Script -ITP 270

import socket
from IPy import IP
import pyfiglet
import subprocess
import time
from datetime import datetime

#Clearing the terminal window
subprocess.call('clear', shell=True)

#Port scanner banner
Port_Scanner_Banner = pyfiglet.figlet_format("PORT SCANNER")
print(Port_Scanner_Banner)

#Adding a one second delay timer
time.sleep(1)

# List to store open ports
ports = []

# List to store discovered banners
banners = []

def scan(target):
    #Defining the scan target function
    converted_ip = convert_ip(target)
    print('\n' + 'Scanning Target : ' + str(target))
    for port in range(int(start_port),int(end_port)):
        scan_port(converted_ip, port)

def convert_ip(ip):
    #Defining function that converts hostname if not already an IP
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

#def get_banner(s):
# Defining function that grabs any port banners and returns data received
#    return s.recv(1024)

def scan_port(ipaddress, port):
    #Defining function that scans target system ports and sets the connection timeout to 0.5 to connect
#(faster but not as accurate, increase number for better accuracy) >> If banner is available, it will
#be collected, unwanted characters stripped out, and printed to terminal >> If port is open, will
#print open port >> If port is closed, pass (print nothing to terminal)
    try:
        sock = socket.socket()
        sock.settimeout(0.1)
        sock.connect((ipaddress, port))

        try:
            banner = get_banner(sock)
            print('[+] Port ' + str(port) + ' is Open ' + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Port ' + str(port) + ' is Open ')
        sock.close()
    except:
        pass

#Defining a split function that scans multiple targets specified with a comma, else scan one specified target
#Line 58 prevents scan function from being called twice if script is imported into another module
if __name__ == "__main__":
    targets = input('[+] Enter target(s) to scan (For multiple targets use a comma): ')
    start_port = input('Enter the port to start the scan: ')
    end_port = input('Enter the port to start the scan: ')
    #check start time
    time_start = datetime.now().replace(microsecond=0)
    print("Scanning started at:" + str(time_start))

    if ',' in targets:
        for ip_address in targets.split(','):
            scan(ip_address.strip(' '))
    else:
        scan(targets)

with open('vulnerable_banners.txt' , 'r') as file:
    count = 0
    for banner in banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT: ' + str(ports[count]))
        count += 1

#check completed time
time_completed = datetime.now().replace(microsecond=0)

#Total time to scan
time_total = time_completed - time_start

print("Scanning ended at:" + str(time_completed))
print("Scanning Completed in " + str(time_total))
