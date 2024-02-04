from lib.finder.shell.shell import *
from lib.finder.wpshell.wpshell import *
import os
import platform
from colorama import Fore, Style, init

init()
red = Fore.RED
green = Fore.LIGHTGREEN_EX
yellow = Fore.YELLOW
reset = Style.RESET_ALL
blue = Fore.BLUE
lightY = Fore.LIGHTYELLOW_EX
cyan = Fore.LIGHTCYAN_EX
space = "   "

def clear():
    operating_system = platform.system()

    if operating_system == 'Windows':
        os.system('cls')
    elif operating_system == 'Linux' or operating_system == 'Darwin': 
        os.system('clear')
    else:
        print("Sistem operasi tidak didukung untuk membersihkan terminal.")



def banner():
    banner = f"""

{space}{space}{space}{lightY}╔═╗╦  ╔═╗╦ ╦  ╔╗ ╔═╗╔╦╗
{space}{space}{space}{lightY}║  ║  ╠═╣╚╦╝  ╠╩╗║ ║ ║ 
{space}{space}{space}{lightY}╚═╝╩═╝╩ ╩ ╩   ╚═╝╚═╝ ╩ \n {reset}
{space}[{green}01{reset}] Shell Finder ({red} 1k+ list name shells {reset})
{space}[{green}02{reset}] Shell Finder CMS Wordpress ({red} All Dir wp {reset})

"""
    print(banner)

def main():
    while True:
        cmd = input(f"{cyan}Input Your Options =>{reset} ")
        if cmd == "01":
            shell()
        if cmd == "02":
            wpshell()
        elif cmd == "exit":
            print("Exiting program")
            break
        else:
            print(f"{red}Are you stupid bro??")
if __name__ == "__main__":
    clear()
    banner()
    main()
