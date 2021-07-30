#!/usr/bin/env bash
# This Programm Write by Mr.nope
# Gmail-Brute Force v1.4.3
if [[ "$(id -u)" -ne 0 ]]; then
 echo "
Please, Run This Programm as Root!"
 exit 1
fi
function main() {
    printf '\033]2;Gmail-Brute Force\a'
    clear
    echo "
Installing..."
    chmod +x crack.py
    sleep 2
    apt install python
    apt install python3
    apt install python3-pip
    pip3 install --upgrade pip
    echo "
Finish ;)

Usage:
      python3 crack.py 
      "
    exit 1
}
main