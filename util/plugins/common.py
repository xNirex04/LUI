import os
import sys
import ctypes
import random
import subprocess
import pylibcheck

from urllib.request import urlopen, urlretrieve
from distutils.version import LooseVersion
from colorama import Fore
from time import sleep

THIS_VERSION = "1.0.0"


@staticmethod
def get_release_version_number(self):
    path = (
        "LATEST_RELEASE"
        if not self.target_version
        else f"LATEST_RELEASE_{self.target_version}"
    )
    return LooseVersion(urlopen(self.__class__.DL_BASE + path).read().decode())

@staticmethod
def get_release_version_number(self):
    path = (
        "LATEST_STABLE"
        if not self.target_version
        else f"LATEST_RELEASE_{str(self.target_version).split('.', 1)[0]}"
    )
    urlretrieve(
        f"{self.__class__.DL_BASE}{path}",
        filename=f"{getTempDir()}\\{path}",
    )
    with open(f"{getTempDir()}\\{path}", "r+") as f:
        _file = f.read().strip("\n")
        content = ""
        for char in [x for x in _file]:
            for num in ("0","1","2","3","4","5","6","7","8","9","."):
                if char == num:
                    content += char
    return LooseVersion(content)


def clear():
    system = os.name
    if system == 'nt':
        #if its windows
        os.system('cls')
    elif system == 'posix':
        #if its linux
        os.system('clear')
    else:
        print('\n'*120)
    return

def setTitle(_str):
    system = os.name
    if system == 'nt':
        #if its windows
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | Made By dnx")
    elif system == 'posix':
        #if its linux
        sys.stdout.write(f"\x1b]0;{_str} | Made By dnx\x07")
    else:
        #if its something else or some err happend for some reason, we do nothing
        pass

def getTempDir():
    system = os.name
    if system == 'nt':
        #if its windows
        return os.getenv('temp')
    elif system == 'posix':
        #if its linux
        return '/tmp/'

def RandomChinese(amount, second_amount):
    name = u''
    for i in range(random.randint(amount, second_amount)):
        name = name + chr(random.randint(0x4E00,0x8000))
    return name

def SlowPrint(_str):
    for letter in _str:
        #slowly print out the words 
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.04)

def installPackage(dependencies):
    print(f'{Fore.CYAN}Checking packages. . .{Fore.RESET}')
    if sys.argv[0].endswith('.exe'):
            #get all installed libs
            reqs = subprocess.check_output(['python', '-m', 'pip', 'freeze'])
            installed_packages = [r.decode().split('==')[0].lower() for r in reqs.split()]

            for lib in dependencies:
                #check for missing libs 
                if lib not in installed_packages:
                    #install the lib if it wasn't found
                    print(f"{Fore.BLUE}{lib}{Fore.RED} not found! Install it. . .{Fore.RESET}")
                    try:
                        subprocess.check_call(['python', '-m', 'pip', 'install', lib])
                    #incase something goes wrong we notify the user that something happend
                    except Exception as e:
                        print(f"{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : {e}")
                        sleep(0.5)
                        pass
    else:
        for i in dependencies:
            if not pylibcheck.checkPackage(i):
                print(f"{Fore.BLUE}{i}{Fore.RED} not found! install it. . .{Fore.RESET}")
                pylibcheck.installPackage(i)

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

                                                            #FADE TYPES#
########################################################################################################################################################
def blackwhite(text):
    os.system(""); faded = ""
    red = 0; green = 0; blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 20; green += 20; blue += 20
            if red > 255 and green > 255 and blue > 255:
                red = 255; green = 255; blue = 255
    return faded

def cyan(text):
    os.system(""); fade = ""
    blue = 100
    for line in text.splitlines():
        fade += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
        if not blue == 255:
            blue += 15
            if blue > 255:
                blue = 255
    return fade

def neon(text):
    os.system(""); fade = ""
    for line in text.splitlines():
        red = 255
        for char in line:
            red -= 2
            if red > 255:
                red = 255
            fade += (f"\033[38;2;{red};0;255m{char}\033[0m")
        fade += "\n"
    return fade

def purple(text):
    os.system(""); fade = "" 
    red = 255
    for line in text.splitlines():
        fade += (f"\033[38;2;{red};0;180m{line}\033[0m\n")
        if not red == 0:
            red -= 20
            if red < 0:
                red = 0
    return fade

def water(text):
    os.system(""); fade = ""
    green = 10
    for line in text.splitlines():
        fade += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return fade

def fire(text):
    os.system(""); fade = ""
    green = 250
    for line in text.splitlines():
        fade += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return fade
########################################################################################################################################################

def getTheme():
    themes = ["green", "black", "fire", "water", "neon"]
    with open(getTempDir()+"\\green_theme", 'r') as f:
        text = f.read()
        if not any(s in text for s in themes):
            print(f'{Fore.RESET}[{Fore.RED}Fehler{Fore.RESET}] : An invalid theme was specified. Switch to default setting. . .')
            setTheme('green')
            sleep(2.5)
            __import__("Generator").main()
        return text

def setTheme(new: str):
    with open(getTempDir()+"\\green_theme", 'w'): pass
    with open(getTempDir()+"\\green_theme", 'w') as f:
        f.write(new)

def banner(theme=None):
    if theme == "black":
        print(bannerTheme(blackwhite, blackwhite))
    elif theme == "fire":
        print(bannerTheme(fire, fire))
    elif theme == "water":
        print(bannerTheme(water, cyan))
    elif theme == "neon":
        print(bannerTheme(purple, neon))
    else:
        print(f'''{Fore.GREEN}

   _____ ______ _   _ ______ _____         _______ ____  _____  
  / ____|  ____| \ | |  ____|  __ \     /\|__   __/ __ \|  __ \ 
 | |  __| |__  |  \| | |__  | |__) |   /  \  | | | |  | | |__) |
 | | |_ |  __| | . ` |  __| |  _  /   / /\ \ | | | |  | |  _  / 
 | |__| | |____| |\  | |____| | \ \  / ____ \| | | |__| | | \ \ 
  \_____|______|_| \_|______|_|  \_\/_/    \_\_|  \____/|_|  \_|


    
> Version : {THIS_VERSION}
                                                                  
> Created by dnx#0007           
> NITRO GENERATOR                                 '''.replace('█', f'{Fore.WHITE}█{Fore.GREEN}') + f'''   
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.RESET}[{Fore.GREEN}1{Fore.RESET}]{Fore.LIGHTBLACK_EX} Nitro Generator                                  
{Fore.RESET}[{Fore.GREEN}2{Fore.RESET}]{Fore.LIGHTBLACK_EX} Credits                  
{Fore.RESET}[{Fore.GREEN}3{Fore.RESET}]{Fore.LIGHTBLACK_EX} Settings            
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')

def bannerTheme(type1, type2):
    return type1(f'''

   _____ ______ _   _ ______ _____         _______ ____  _____  
  / ____|  ____| \ | |  ____|  __ \     /\|__   __/ __ \|  __ \ 
 | |  __| |__  |  \| | |__  | |__) |   /  \  | | | |  | | |__) |
 | | |_ |  __| | . ` |  __| |  _  /   / /\ \ | | | |  | |  _  / 
 | |__| | |____| |\  | |____| | \ \  / ____ \| | | |__| | | \ \ 
  \_____|______|_| \_|______|_|  \_\/_/    \_\_|  \____/|_|  \_|



> Version : {THIS_VERSION}

> Created by dnx#0023           
> NITRO GENERATOR                                 ''')+type2('''  
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[1] Nitro Generator                                   
[2] Credits                  
[3] Settings              
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')
