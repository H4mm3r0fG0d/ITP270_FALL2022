#Importing necessary libraries.
import socket
import subprocess
import time
import sys
import pyfiglet

subprocess.call('clear', shell=True)

#Creating a script banner.
Port_Scan_Banner = pyfiglet.figlet_format("PORT SCANNER")
print(Port_Scan_Banner)

time.sleep(1)

#Use of sockets module to take user input and use in script to talk to network and find host.
Remote_Server = input("Enter an IP address to scan: ")
target = socket.gethostbyname(Remote_Server)

#Brief explanation for user while scan is in process.
print("_" * 50)
print("Scanning the following host: " + target)
print("_" * 50)

#Creating the scanning loop. Connect to socket and set target IP to test for open ports.
try:

    for port in range (1, 4000):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = s.connect_ex((target, port))

        if result == 0:

            print ("Port {}: is open".format(port))

            s.close()

#Exception response in event of keyboard interrupt.
except KeyboardInterrupt:
    print("\n The scan was canceled.")
    sys.exit()

#Exception response in event of invalid IP
except socket.gaierror:
    print("\n Hostname could not be resolved.")
    sys.exit()

#Exception response in event of socket error.
except socket.error:
    print("\n No response.")
    sys.exit()

#End of script.