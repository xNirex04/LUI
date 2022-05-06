import multiprocessing
import keyboard
import base64

from util.plugins.common import *
from util.plugins.update import search_for_updates
import util.info

threads = 3
cancel_key = "ctrl+x"

def main():
    setTitle(f"Logged Project {THIS_VERSION}")
    clear()
    global threads
    global cancel_key
    if getTheme() == "green":
        banner()
    elif getTheme() == "schwarz":
        banner("schwarz")
    elif getTheme() == "feuer":
        banner("feuer")
    elif getTheme() == "wasser":
        banner("wasser")
    elif getTheme() == "neon":
        banner("neon")

    choice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Auswahl: {Fore.RED}')
    #all options
    if choice == "1":
        import ctypes
        import string
        import os
        import time
        LICNECE = """
        Copyright (c) 2021 Drillenissen#4268 logicguy.mailandcontact@gmail.com
        Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
        The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
        THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
        try:  # Setup try statement to catch the error
            import requests  # Try to import requests
        except ImportError:  # If it has not been installed
    # Tell the user it has not been installed and how to install it
            input(
                f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
            exit()  # Exit the program
        try:  # Setup try statement to catch the error
            import numpy  # Try to import requests
        except ImportError:  # If it has not been installed
    # Tell the user it has not been installed and how to install it
            input(
                f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
            exit()  # Exit the program

# check if user is connected to internet
        url = "https://github.com"
        try:
            response = requests.get(url)  # Get the responce from the url
            print("Internet check")
            time.sleep(.4)
        except requests.exceptions.ConnectionError:
    # Tell the user
            input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
            exit()  # Exit program


        class NitroGen:  # Initialise the class
            def __init__(self):  # The initaliseaiton function
                self.fileName = "Nitro Codes.txt"  # Set the file name the codes are stored in

            def main(self):  # The main function contains the most important code
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
                if os.name == "nt":  # If the system is windows
                    print("")
                    ctypes.windll.kernel32.SetConsoleTitleW(
                        "Nitro Generator and Checker - Made by Drillenissen#4268")  # Change the
                else:  # Or if it is unix
                    print(f'\33]0;Nitro Generator and Checker - Made by Drillenissen#4268\a',
                        end='', flush=True)  # Update title of command prompt

                print("""
   _____ ______ _   _ ______ _____         _______ ____  _____  
  / ____|  ____| \ | |  ____|  __ \     /\|__   __/ __ \|  __ \ 
 | |  __| |__  |  \| | |__  | |__) |   /  \  | | | |  | | |__) |
 | | |_ |  __| | . ` |  __| |  _  /   / /\ \ | | | |  | |  _  / 
 | |__| | |____| |\  | |____| | \ \  / ____ \| | | |__| | | \ \ 
  \_____|______|_| \_|______|_|  \_\/_/    \_\_|  \____/|_|  \_|
                                                                
                                                                
                                                        """)  # Print the title card
                time.sleep(2)  # Wait a few seconds
        # Print who developed the code
                self.slowType("Made by: Drillenissen#4268 && Benz#1131", .02)
                time.sleep(1)  # Wait a little more
        # Print the first question
                self.slowType(
                    "\nInput How Many Codes to Generate and Check: ", .02, newLine=False)

                try:
                    num = int(input(''))  # Ask the user for the amount of codes
                except ValueError:
                    input("Specified input wasn't a number.\nPress enter to exit")
                    exit()  # Exit program

                if USE_WEBHOOK:
            # Get the webhook url, if the user does not wish to use a webhook the message will be an empty string
                    self.slowType(
                        "If you want to use a Discord webhook, type it here or press enter to ignore: ", .02, newLine=False)
                    url = input('')  # Get the awnser
            # If the url is empty make it be None insted
                    webhook = url if url != "" else None
            
                    if webhook is not None:
                        DiscordWebhook(  # Let the user know it has started logging the ids
                                url=url,
                                content=f"```Started checking urls\nI will send any valid codes here```"
                            ).execute()

        # print() # Print a newline for looks

                valid = []  # Keep track of valid codes
                invalid = 0  # Keep track of how many invalid codes was detected
                chars = []
                chars[:0] = string.ascii_letters + string.digits

        # generate codes faster than using random.choice
                c = numpy.random.choice(chars, size=[num, 23])
                for s in c:  # Loop over the amount of codes to check
                    try:
                        code = ''.join(x for x in s)
                        url = f"https://discord.gift/{code}"  # Generate the url

                        result = self.quickChecker(url, webhook)  # Check the codes

                        if result:  # If the code was valid
                    # Add that code to the list of found codes
                            valid.append(url)
                        else:  # If the code was not valid
                            invalid += 1  # Increase the invalid counter by one
                    except KeyboardInterrupt:
                # If the user interrupted the program
                        print("\nInterrupted by user")
                        break  # Break the loop

                    except Exception as e:  # If the request fails
                        print(f" Error | {url} ")  # Tell the user an error occurred

                    if os.name == "nt":  # If the system is windows
                        ctypes.windll.kernel32.SetConsoleTitleW(
                            f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268")  # Change the title
                        print("")
                    else:  # If it is a unix system
                # Change the title
                        print(
                            f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268\a', end='', flush=True)

                print(f"""
        Results:
        Valid: {len(valid)}
        Invalid: {invalid}
        Valid Codes: {', '.join(valid)}""")  # Give a report of the results of the check

        # Tell the user the program finished
                input("\nThe end! Press Enter 5 times to close the program.")
                [input(i) for i in range(4, 0, -1)]  # Wait for 4 enter presses

    # Function used to print text a little more fancier
            def slowType(self, text: str, speed: float, newLine=True):
                for i in text:  # Loop over the message
            # Print the one charecter, flush is used to force python to print the char
                    print(i, end="", flush=True)
                    time.sleep(speed)  # Sleep a little before the next one
                if newLine:  # Check if the newLine argument is set to True
                    print()  # Print a final newline to make it act more like a normal print statement

            def quickChecker(self, nitro:str, notify=None):  # Used to check a single code at a time
        # Generate the request url
                url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
                response = requests.get(url)  # Get the response from discord

                if response.status_code == 200:  # If the responce went through
            # Notify the user the code was valid
                    print(f" Valid | {nitro} ", flush=True,
                        end="" if os.name == 'nt' else "\n")
                    with open("Nitro Codes.txt", "w") as file:  # Open file to write
                # Write the nitro code to the file it will automatically add a newline
                        file.write(nitro)

                    if notify is not None:  # If a webhook has been added
                        DiscordWebhook(  # Send the message to discord letting the user know there has been a valid nitro code
                            url=url,
                            content=f"Valid Nito Code detected! @everyone \n{nitro}"
                        ).execute()

                    return True  # Tell the main function the code was found

        # If the responce got ignored or is invalid ( such as a 404 or 405 )
                else:
            # Tell the user it tested a code and it was invalid
                    print(f" Invalid | {nitro} ", flush=True,
                        end="" if os.name == 'nt' else "\n")
                    return False  # Tell the main function there was not a code found


        if __name__ == '__main__':
            Gen = NitroGen()  # Create the nitro generator object
            Gen.main()  # Run the main code

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
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Setting: {Fore.RED}')
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
                setTheme('schwarz')
            elif themechoice == "3":
                setTheme('feuer')
            elif themechoice == "4":
                setTheme('wasser')
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
    if os.path.basename(sys.argv[0]).endswith("exe"):
        search_for_updates()
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
