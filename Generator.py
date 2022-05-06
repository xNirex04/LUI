from util.plugins.common import *
from util.plugins.update import search_for_updates

threads = 3
cancel_key = "ctrl+x"

def main():
    setTitle(f"NITRO GENERATOR {THIS_VERSION}")
    clear()
    global threads
    global cancel_key
    if getTheme() == "green":
        banner()
    elif getTheme() == "black":
        banner("black")
    elif getTheme() == "fire":
        banner("fire")
    elif getTheme() == "water":
        banner("water")
    elif getTheme() == "neon":
        banner("neon")

    choice = input(
            f'{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.RESET}Choice: {Fore.RED}')
    #all options
    if choice == "1":
        import ctypes
        import string
        import os
        import time
        LICNECE = """
        Copyright (c) 2021 dnx#0023

        THIS TOOL IS FROM BLACK X DISCORD SERVER, THIS TOOL STATUS IS FREE AND IS NOT TOO OP!!

        """

        USE_WEBHOOK = True

        print(LICNECE)

        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')


        try:
            from discord_webhook import DiscordWebhook
        except ImportError:
            input(
                f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
            USE_WEBHOOK = False
        try: 
            import requests  
        except ImportError:  
            input(
                f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
            exit()  
        try:  
            import numpy  
        except ImportError:  
            input(
                f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
            exit()

        url = "https://github.com"
        try:
            response = requests.get(url) 
            print("Internet check")
            time.sleep(.4)
        except requests.exceptions.ConnectionError:
            input(f"{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.YELLOW}You are not connected to internet, check your connection and try again {Fore.RESET}/ {Fore.CYAN}Press Enter to Exit")
            sleep(1.5)
            main() 


        class NitroGen:
            def __init__(self):
                self.fileName = "Nitro Codes.txt" 

            def main(self): 
                os.system('cls' if os.name == 'nt' else 'clear') 
                if os.name == "nt": 
                    print("")
                    ctypes.windll.kernel32.SetConsoleTitleW(
                        f"Nitro Generator - Version {THIS_VERSION}") 
                else: 
                    print(f'\33]0;Nitro Generator -Version {THIS_VERSION}\a',
                        end='', flush=True)

                print("""
    ,------.  ,--.  ,--.,--.   ,--. 
    |  .-.  \ |  ,'.|  | \  `.'  /    .̸̺̓̉̾͊̕N͓̽I͓̽T͓̽R͓̽O͓̽.̸̺̓̉̾͊̕
    |  |  \  :|  |' '  |  .'    \     .̸̺̓̉̾͊̕2͓̽0͓̽2͓̽2͓̽.̸̺̓̉̾͊̕
    |  '--'  /|  | `   | /  .'.  \    .̸̺̓̉̾͊̕.̸̺̓̉̾͊̕.̸̺̓̉̾͊̕ FREE VERSION.̸̺̓̉̾͊̕.̸̺̓̉̾͊̕
    `-------' `--'  `--''--'   '--'  
                                                                
                                                                
                                                        """) 
                time.sleep(2)
                self.slowType(f"{Fore.CYAN}Version : {THIS_VERSION}", .02)
                time.sleep(1)
                self.slowType(
                    f"\n{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.CYAN}Input How Many Codes to Generate: {Fore.RESET}", .02, newLine=False)

                try:
                    num = int(input(''))
                except ValueError:
                    input(f"{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.YELLOW}Specified input wasn't a number {Fore.RESET}/ {Fore.CYAN}Press enter to exit")
                    sleep(1.5)
                    main()

                if USE_WEBHOOK:
                    self.slowType(
                        f"{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.CYAN}If you want to use a Discord webhook, type it here or press enter to ignore: {Fore.RESET}", .02, newLine=False)
                    url = input('') 
                    webhook = url if url != "" else None
            
                    if webhook is not None:
                        DiscordWebhook( 
                                url=url,
                                content=f"```STARTED!\nI will send any valid codes here in```"
                            ).execute()


                valid = []
                invalid = 0 
                chars = []
                chars[:0] = string.ascii_letters + string.digits

                c = numpy.random.choice(chars, size=[num, 23])
                for s in c: 
                    try:
                        code = ''.join(x for x in s)
                        url = f"https://discord.gift/{code}"

                        result = self.quickChecker(url, webhook) 

                        if result: 
                            valid.append(url)
                        else:  
                            invalid += 1  
                    except KeyboardInterrupt:
                        print("\nInterrupted by user")
                        break 

                    except Exception as e: 
                        print(f" Error | {url} ") 

                    if os.name == "nt":
                        ctypes.windll.kernel32.SetConsoleTitleW(
                            f"Nitro Generator - {len(valid)} Valid | {invalid} Invalid - Made by dnx#0023") 
                        print("")
                    else: 
                        print(
                            f'\33]0;Nitro Generator - {len(valid)} Valid | {invalid} Invalid - Made by dnx#0023\a', end='', flush=True)

                print(f"""
        Results:
        Valid: {len(valid)}
        Invalid: {invalid}
        Valid Codes: {', '.join(valid)}""") 

                input(f"\n{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.CYAN}The end! Press Enter to Exit.")
                sleep(1.5)
                main()

            def slowType(self, text: str, speed: float, newLine=True):
                for i in text:
                    print(i, end="", flush=True)
                    time.sleep(speed)
                if newLine:
                    print() 

            def quickChecker(self, nitro:str, notify=None): 
                url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
                response = requests.get(url)

                if response.status_code == 200:
                    print(f"{Fore.GREEN}[{Fore.MAGENTA}>{Fore.GREEN}] {Fore.MAGENTA} Valid {Fore.RESET}| {Fore.CYAN}{nitro} ", flush=True,
                        end="" if os.name == 'nt' else "\n")
                    with open("Nitro Codes.txt", "w") as file:
                        file.write(nitro)

                    if notify is not None: 
                        DiscordWebhook( 
                            url=url,
                            content=f"Valid Nito Code! @everyone \n{nitro}"
                        ).execute()

                    return True 

                else:
                    print(f"{Fore.GREEN}[{Fore.RED}+{Fore.GREEN}] {Fore.RED}Invalid {Fore.RESET}| {Fore.CYAN}{nitro} ", flush=True,
                        end="" if os.name == 'nt' else "\n")
                    return False


        if __name__ == '__main__':
            Gen = NitroGen() 
            Gen.main()

    elif choice == '2':
        print(f"{Fore.CYAN}CREDITS:\n{Fore.RESET} {Fore.BLUE} Link: {Fore.RESET} https://discord.com/invite/qXMjpXFgWG")
        sleep(4)
        main()


    elif choice == '3':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Theme Changer
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Count of Threads
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] Exit Button
    {Fore.RESET}[{Fore.RED}4{Fore.RESET}] {Fore.RED}Exit...    
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.RESET}Setting: {Fore.RED}')
        if secondchoice not in ["1", "2", "3", "4"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Settings')
            sleep(1)
            main()
        if secondchoice == "1":
            print(f"""
{Fore.GREEN}Green: 1
{Fore.LIGHTBLACK_EX}Black: 2
{Fore.RED}Fire: 3
{Fore.BLUE}Water: 4
{Fore.CYAN}N{Fore.MAGENTA}e{Fore.CYAN}o{Fore.MAGENTA}n{Fore.CYAN}:{Fore.MAGENTA} 5
""")
            themechoice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}theme: {Fore.RED}')
            if themechoice == "1":
                setTheme('green')
            elif themechoice == "2":
                setTheme('black')
            elif themechoice == "3":
                setTheme('fire')
            elif themechoice == "4":
                setTheme('water')
            elif themechoice == "5":
                setTheme('neon')
            else:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Theme')
                sleep(1.5)
                main()
            SlowPrint(f"{Fore.GREEN}Theme has set to {Fore.CYAN}{getTheme()}")
            sleep(0.5)
            main()

        elif secondchoice == "2":
            print(f"{Fore.BLUE}Current count of Threads: {threads}")
            try:
                amount = int(
                    input(f'{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.RESET}Count of Threads: {Fore.RED}'))
            except ValueError:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : invalid amount')
                sleep(1.5)
                main()
            if amount >= 45:
                print(f"{Fore.RED}I'm sorry but if you want to have that many threads you'll only get rate limited and end up no good")
                sleep(3)
                main()
            elif amount >= 15:
                print(f"{Fore.RED}WARNING! * WARNING! * WARNING!")
                print(f"If the thread count is set to 15 or more, you may experience lag and a higher chance of rate limiting\nare you sure you want to set the rate limit to {Fore.YELLOW}{amount}{Fore.RED}?")
                yesno = input(f'{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.RESET}yes/no: {Fore.RED}')
                if yesno.lower() != "yes":
                    sleep(0.5)
                    main()
            threads = amount
            SlowPrint(f"{Fore.GREEN}Threads set to {Fore.CYAN}{amount}")
            sleep(0.5)
            main()
        
        elif secondchoice == "3":
            print("\n","Info".center(30, "-"))
            print(f"{Fore.CYAN}Currently Cancle Key: {cancel_key}")
            print(f"""{Fore.BLUE}If you want ctrl + <key> you have to type out ctrl+<key> | DO NOT literally press ctrl + <key>
{Fore.GREEN}Example: shift + Q

{Fore.RED}You can also use other modifiers instead of Ctrl ⇣
{Fore.YELLOW}All Keyboard Modifiers:{Fore.RESET}
ctrl, shift, enter, esc, windows, left shift, right shift, left ctrl, right ctrl, alt gr, left alt, right alt
""")
            sleep(1.5)
            key = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Taste: {Fore.RED}')
            cancel_key = key
            SlowPrint(f"{Fore.GREEN}Exit Button set to {Fore.CYAN}{cancel_key}")
            sleep(0.5)
            main()

        elif secondchoice == "4":
            setTitle("Exit. . .")
            choice = input(
                f'{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.RESET}Are you sure you want to end this? (Y to confirm): {Fore.RED}')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                clear()
                os._exit(0)
            else:
                main()
    else:
        clear()
        main()

if __name__ == "__main__":
    import sys
    search_for_updates()
    if os.path.basename(sys.argv[0]).endswith("exe"):
        if not os.path.exists(getTempDir()+"\\green_theme"):
            setTheme('green')
        clear()
        sleep(1.5)
        main()
    try:
        assert sys.version_info >= (3,8)
    except AssertionError:
        print(f"{Fore.RED}Your Python-Version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with Logged Project, please download Python 3.7+")
        sleep(5)
        print("verlassen. . .")
        sleep(1.5)
        os._exit(0)
    else:
        search_for_updates()
        if not os.path.exists(getTempDir()+"\\green_theme"):
            setTheme('green')
        clear()
        sleep(1.5)
        main()
    finally:
        Fore.RESET
