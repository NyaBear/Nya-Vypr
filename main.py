import requests
import sys
import colorama
from colorama import Fore, Back, Style
import os
import logging

def introduction():
    print(Fore.MAGENTA + """

 ███▄    █▓██   ██▓ ▄▄▄          ██▒   █▓▓██   ██▓ ██▓███   ██▀███  
 ██ ▀█   █ ▒██  ██▒▒████▄       ▓██░   █▒ ▒██  ██▒▓██░  ██▒▓██ ▒ ██▒
▓██  ▀█ ██▒ ▒██ ██░▒██  ▀█▄      ▓██  █▒░  ▒██ ██░▓██░ ██▓▒▓██ ░▄█ ▒
▓██▒  ▐▌██▒ ░ ▐██▓░░██▄▄▄▄██      ▒██ █░░  ░ ▐██▓░▒██▄█▓▒ ▒▒██▀▀█▄  
▒██░   ▓██░ ░ ██▒▓░ ▓█   ▓██▒      ▒▀█░    ░ ██▒▓░▒██▒ ░  ░░██▓ ▒██▒
░ ▒░   ▒ ▒   ██▒▒▒  ▒▒   ▓▒█░      ░ ▐░     ██▒▒▒ ▒▓▒░ ░  ░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░▓██ ░▒░   ▒   ▒▒ ░      ░ ░░   ▓██ ░▒░ ░▒ ░       ░▒ ░ ▒░
   ░   ░ ░ ▒ ▒ ░░    ░   ▒           ░░   ▒ ▒ ░░  ░░         ░░   ░ 
         ░ ░ ░           ░  ░         ░   ░ ░                 ░     
           ░ ░                       ░    ░ ░                        
""")
    print(Style.RESET_ALL)

introduction()


print(Fore.CYAN + "[ ! ] Hello, This tool lets you check if your Vypr VPN account is valid or invalid. ( Personal Use Only )")
print(Style.RESET_ALL)

print(Fore.LIGHTYELLOW_EX + "Please enter your Email: ")
username_input = input("[ > ] ")

print(Fore.LIGHTYELLOW_EX + "Please enter your Password: ")
password_input = input("[ > ] ")

def logic(username, password):
    headers = {
        "Pragma": "no-cache",
        "Accept": "*/*",
        "X-GF-PLATFORM": "Windows",
        "X-GF-PRODUCT": "VyprVPN",
        "X-GF-PLATFORM-VERSION": "Windows v10.0 build(18362) X64",
        "X-GF-PRODUCT-VERSION": "2.16.4.9212",
        "username": username,
        "password": password,
        "X-GF-Agent": "VyprVPN Windows 2.16.4.9212 (ABB444E5)",
        "locale": "en"
    }
    r = requests.get("https://api.goldenfrog.com/settings", headers=headers)
    response = (r.status_code)
    if response == 200:
        jsonval = r.json()
        plan = jsonval["vpn"]["account_level"]
        print("")
        print(Fore.LIGHTGREEN_EX + "This account is Valid")
        print("Plan: " + plan)
        print(Style.RESET_ALL)
        print("")
        input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
        print(Style.RESET_ALL)
        sys.exit(0)
    elif response == 403:
        print("")
        print(Fore.LIGHTRED_EX + "This account is Invalid")
        print(Style.RESET_ALL)
        print("")
        input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
        print(Style.RESET_ALL)
        sys.exit(0)
    else:
        print("")
        print("Something went wrong, perhaps your username is invalid or something regarding your network.")
        input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
        print(Style.RESET_ALL)
        sys.exit(0)

logic(username_input, password_input)
