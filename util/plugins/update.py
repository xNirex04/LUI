import requests
import os
import shutil
import re
import sys

from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.common import *

def search_for_updates():
    clear()
    setTitle("Nitro Generator is checking for Update. . .")
    r = requests.get("https://github.com/xNirex04/UZ/releases/latest")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        setTitle("Nitro Generator found an new Update!")
        print(f'''{Fore.YELLOW}
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                              {Fore.RED}Looks like the Nitro Generator {THIS_VERSION} is expired '''.replace('█', f'{Fore.WHITE}█{Fore.RED}'), end="\n\n")
        soup = BeautifulSoup(requests.get("https://github.com/xNirex04/UZ/releases/latest").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        choice = input(
            f'{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.RESET}Would you like to Download the new Update? (Press "Y" to Update): {Fore.RED}')

        if choice.lower() == 'y' or choice.lower() == 'yes':
            print(f"{Fore.WHITE}\nUpdating. . .")
            setTitle(f'Nitro Generator Updating...')
            #if they are running hazard.exe
            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("GeneratorRealese.zip", 'wb')as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("GeneratorRealese.zip", 'r') as filezip:
                    filezip.extractall()
                cwd = os.getcwd()+'\\GeneratorRealese\\'
                shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                try:
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), 'Logged.exe')
                except Exception:
                    pass
                shutil.copyfile(cwd+'README.md', 'README.md')                   
                shutil.rmtree('GeneratorRealese')
                setTitle('Nitro Generator Update done!')
                print(f"{Fore.GREEN}Update successfully installed!")
                sleep(2)
                os.startfile("Generator.exe")
                os._exit(0)