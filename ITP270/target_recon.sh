#!/bin/bash

echo "Enter first name: "
read first_name

echo "Enter last name: "
read last_name

echo "Enter State/Province: "
read location

echo "Searching for " $first_name $last_name $location

firefox "https://www.411.com/name/$first_name-$last_name?/$location?/" &
sleep 1
firefox --new-tab "https://www.peekyou.com/usa/$location/$first_name"_"$last_name" &
sleep 1
firefox --new-tab "https://www.ontheissues.org/Profile_$first_name"_"$last_name.htm" &
sleep 1
firefox --new-tab "https://www.search.wikileaks.org/?query=$location&exact_phrase=$first_name+$last_name" &
sleep 1
firefox --new-tab "https://www.azquotes.com/search_results.html?query=$first_name+$last_name" &
