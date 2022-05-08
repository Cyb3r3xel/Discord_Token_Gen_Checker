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


██████████████████████████████████████▀█████████████████████████████████████████████████████████
█─▄─▄─█─▄▄─█▄─█─▄█▄─▄▄─█▄─▀█▄─▄███─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄███─▄▄▄─█─█─█▄─▄▄─█─▄▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█
███─███─██─██─▄▀███─▄█▀██─█▄▀─████─██▄─██─▄█▀██─█▄▀─████─███▀█─▄─██─▄█▀█─███▀██─▄▀███─▄█▀██─▄─▄█
▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀ \n\n'''+ Fore.RESET + Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]\n")
 
os.system("cls")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
    
print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
print(Fore.WHITE +Fore.BLUE +"                                         Welcome to "+Fore.WHITE+" Token-Gen "+Fore.WHITE+"- 2022 -")
print(Fore.WHITE +Fore.BLUE +"                                         [1] "+Fore.WHITE+"Token Generator")
print(Fore.WHITE +Fore.BLUE +"                                         [2] "+Fore.WHITE+"Generated Tokens Checker")
print(Fore.WHITE +Fore.BLUE +"                                         [3] "+Fore.WHITE+"Manual Token Checker(Copy & Paste)")
print(Fore.WHITE +Fore.BLUE +"                                         [4] "+Fore.WHITE+"Credits")
print(Fore.WHITE +Fore.BLUE +"                                         [5] "+Fore.WHITE+"Exit")
print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
opcion = input("\nChoice: ")
if opcion=='1':
  print(fr"""

██████████████████████████████████████▀███████████████
█─▄─▄─█─▄▄─█▄─█─▄█▄─▄▄─█▄─▀█▄─▄███─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄█
███─███─██─██─▄▀███─▄█▀██─█▄▀─████─██▄─██─▄█▀██─█▄▀─██
▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀
                                                                                           {Fore.CYAN}
{Fore.RESET} 
""")
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
                                                                                           {Fore.CYAN}Copy & Paste Your Tokens To Check
{Fore.RESET} 
""")
 from requests import get,post
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
        input('Can`t Open "Generated.txt" File!')
if opcion=='3':
 
if opcion=='4':
    os.system("cls")
    print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
    print(Fore.WHITE +Fore.BLUE +"                                         Token-Gen"+Fore.WHITE+" Made by "+Fore.BLUE+"???")
    print(Fore.WHITE +Fore.BLUE +"                                         [Discord] "+Fore.BLUE+"???")
    print(Fore.WHITE +Fore.BLUE +"                                         [Server] "+Fore.BLUE+"Soon")
    print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
    input(Fore.BLUE +Fore.BLUE +"\nEnter to exit")
    os.system("cls")
    print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
    print(Fore.BLUE +Fore.BLUE +"                                                   Closing!")
    print(Fore.GREEN +Fore.BLUE +"                                               Have a good day!")
    print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
    time.sleep(2)
    sys.exit()
    pass
if opcion=='5':
    os.system("cls")
    print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
    print(Fore.BLUE +Fore.BLUE +"                                                   Closing!")
    print(Fore.GREEN +Fore.BLUE +"                                               Have a good day :D")
    print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.BLUE +"+"+Fore.WHITE +Fore.BLUE +"]"+ Fore.WHITE +Fore.BLUE +"-------------------------------------------------------"+ Fore.WHITE +Fore.BLUE +"["+ Fore.WHITE +Fore.BLUE +"+"+ Fore.WHITE +Fore.BLUE +"]")
    time.sleep(2)
    sys.exit()
    pass
