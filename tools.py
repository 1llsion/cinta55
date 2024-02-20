from plugins.hdinfo.info import *
from plugins.shell.find import *
from lib.colors.colors import *
from plugins.sitemap.map import *
from plugins.ddos.ddos import *
from plugins.ddos.ddoswp import *
from plugins.wpload.scan import *
import os
import platform


class MainProgram:
    def __init__(self):
        self.colors = Colors()
    def auto_clean():
        system_platform = platform.system()

        if system_platform == "Windows":
            os.system("cls")
        elif system_platform == "Linux":
            os.system("clear")
        else:
            print("Unsupported operating system.")
    def Mainbanner():
        space = "   "*5
        space1= "   "
        banner = f"""
{space}{colors.cyan}            
{space}           ^55!.        .!55^           
{space}        :5#G!      .       !G#5:        
{space}      !#@&?.                .?&@#!      
{space}    ^&@@#^         .   :.     ~#@@#^    
{space}   Y@@@#:          ^   5Y7.    :#@@@Y   
{space}  !@@@@~           J.  !^       !@@@@!  
{space}  7@@@@~           P.           ~@@@@7  
{space}   #@@@#:          ?.          :#@@@#   
{space}   !@@@@&!..!?.   ^. ^   .?!..!&@@@@!   
{space}   !@@&&@@5  .YBGGY  YBGBY.  5@@&&@@!   
{space}  :5?JYY?!~.    :5G55P5:    .~!?YYJ?Y:  
{space} .~ B@@@@@#Y^ .7JJ&@@&JJ7. ^Y#@@@@@B ~. 
{space} .P:@@@@@@@@@BJ?55#5Y#55??B@@@@@@@@@:P. 
{space}  !5G#&@@@@@@@@@!!?::?!!@@@@@@@@@&#G5!  
{space}  ?#:YGPY?7Y#@#?57G@@G75?#@#Y7?YPGY:#?  
{space}  7&G7!?YY?!..:?G&@@@@&G?:.:!?YY?!7G&7  
{space}   ~5B&G5BG^.^5P@@@@@@@@P5^.~GBYG#BY~   
{space}      :7^#&Y  ?G5GB&@#G5G?  Y&#^!:      
{space}       &P !7: .^7!^..^!!^. :7! P&       
{space}       ?@Y.^Y^^... ^. ...~^Y^.Y@?       
{space}      .::#~^^77??Y?YJ?Y?J77^^~#::.      
{space}      ~~ !7^ . . ~.^^.~ . . ^7! ~^      
{space}      .?^ ~?!!.:.. .....:.!!?~ ^?.      
{space}       .77. ^^J?J7~~~~7J?J^^ .?7.       
{space}         :?!. ..:^:~~:^:.. .!?:         
{space}           .~~:.   .:   .:~~.           
{space}              ............              \n{colors.reset}
{space1}{colors.green}[{colors.red} 1 {colors.green}]{colors.reset} Shell finder ({colors.red}1k{colors.reset} Wordlist)
{space1}{colors.green}[{colors.red} 2 {colors.green}]{colors.reset} Sitemap Generator
{space1}{colors.green}[{colors.red} 3 {colors.green}]{colors.reset} Takedown Site With DDOS / BOTNET
{space1}{colors.green}[{colors.red} 4 {colors.green}]{colors.reset} Shell Wordpress finder ( all dir )
{space1}{colors.green}[{colors.red} 5 {colors.green}]{colors.reset} Backlink generator ({colors.red} Cooming Soon {colors.reset})
{space1}{colors.green}[{colors.red} 6 {colors.green}]{colors.reset} AMP Generator ({colors.red} Maintenance {colors.reset})
{space1}{colors.green}[{colors.red} 7 {colors.green}]{colors.reset} TUNNEL Generator ({colors.red} Maintenance {colors.reset})
{space1}{colors.green}[{colors.red} 8 {colors.green}]{colors.reset} Scan Vuln Takedown Sites Wordpress 
{space1}{colors.green}[{colors.red} 9 {colors.green}]{colors.reset} GASS TAKEDOWN WP 
{space1}{colors.green}[{colors.red} 10 {colors.green}]{colors.reset} HEADERS INFORMATION
        """
        print(banner)
        
if __name__ == "__main__":
    MainProgram.auto_clean()
    MainProgram.Mainbanner()
    cmd = None

    while cmd != "exit":
        cmd = input(f"{colors.blue}Input Your Option => {colors.reset}")

        if cmd == "1":
            mainscan()
        elif cmd == "2":
            map()
        elif cmd == "3":
            TakeDown()
        elif cmd == "8":
            web_scanner = WebScanner()
            web_scanner.scan_websites()
        elif cmd == "9":
            attackanying()
        elif cmd == "10":
            hdinfo()
        elif cmd.lower() == "exit":
            print(f'{colors.yellow}Exiting the program.{colors.reset}')
        else:
            print(f'{colors.yellow}Invalid input. Please enter a valid option or "exit" to quit.{colors.reset}')
