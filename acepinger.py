#Importing Modules | AcePinger |

try:

	from easygui import fileopenbox, msgbox

	import os

	import time

	from colorama import Fore, Back, Style

	import platform

	from urllib import request

	import sys

except:

	import os

	os.system("pip install easygui requests colorama")

	from easygui import fileopenbox

	from colorama import Fore, Back, Style

	import sys
	
	from urllib import request

def clear():

	if platform.system() == "Linux" or platform.system() == "Darwin":

		os.system("clear")

	elif platform.system() == "Windows":

		os.system("cls")

def ping(url):

	try:

		headers1 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\

            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}

		req = request.urlopen(url)

		a = req.read()

		respo = req.getcode()

		if respo == 200:

			print(f"{Fore.CYAN}{url}{Fore.GREEN} -- Status : OK")

			with open("Good_Urls.txt", "a") as goodfile:

				goodfile.write(url)

		elif respo == 301:

			print(f"{Fore.YELLOW}{url}{Fore.RED} -- Status : Moved Permanently")

		elif respo == 404:

			print(f"{Fore.YELLOW}{url}{Fore.RED} -- Status : Page Not Found")

		elif respo == 403:

                	print(f"{Fore.YELLOW}{url}{Fore.RED} -- Status : Forbidden")

		elif respo == 400:

                	print(f"{Fore.YELLOW}{url}{Fore.RED} -- Status : Bad Request")

		elif respo == 500:

                	print(f"{Fore.YELLOW}{url}{Fore.RED} -- Status : Internal Server Error")

		elif respo == 502:

                	print(f"{Fore.YELLOW}{url}{Fore.RED} -- Status : Bad Gateway")

	except:

		msgbox("Error Occured, Please Re-Run The Program", "AcePinger")

		sys.exit(1)

if __name__ == "__main__":

	clear()

	print(f"{Fore.MAGENTA}Welcome To {Fore.CYAN}ACE PINGER")

	urlsuser = fileopenbox("Open Urls To Scan", "AcePinger", multiple=False)

	clear()

	with open(urlsuser, "r") as file:

		allurls = file.readlines()

		for uurls in allurls:

			ping(uurls)

