#!/usr/bin/bash

title=$1
name=$2
lastname=$3

user=$(whoami)
directory=$(pwd)
time=$(date)

echo "Good morning, $title $lastname"

sleep 1

echo "You're looking lovely today, $name"

sleep 1

echo "What type of beverage are you drinking today?"

read beverage

echo "Let's take a look... That's the most incredible $beverage I've ever seen, $title $name $lastname!"

sleep 1

echo "Alright, down to business $title $lastname. You are logged in as $user in the directory $directory on $time. You can find your assignment in the folder on your desk, courtesy of the IT guys (give them some love later, yeah?). It's not too hard, are you'll be done in the hour.
Have a lovely day,
~Morning Bot Barbara"

sleep 1