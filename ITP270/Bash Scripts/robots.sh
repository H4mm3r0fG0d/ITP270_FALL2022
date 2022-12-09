#!/bin/bash

cd /home/diegokendall/Documents/ITP270_FALL2022/ITP270

echo "Enter a domain: "
read domain

wget -O $domain\ robots.txt  $domain/robots.txt

cat $domain\ robots.txt | grep 'Disallow' | cut -d ' ' -f2 | tr -d "*." > $domain\ robocut.txt 

firefox &
sleep 5

for i in $(cat $domain\ robocut.txt); do
	firefox --new-tab https://www.$domain$i &
	sleep 2
done
