#!/bin/bash

echo "Please enter an IP address: "

read ip_address

nmap -A -sV -vv $ip_address -oN nmap_output.txt
