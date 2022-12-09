#!/bin/bash

echo "Enter an IP address: "

read ip_address

nmap -Pn -sV -vv $ip_address -oN nmap_output.txt
