import subprocess
import os
import sys
import time
from bs4 import BeautifulSoup
import requests


class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
	
def third_step():
    print bcolors.OKGREEN + "\n############*******************START MODE ANONYMOUS **********************############" + bcolors.ENDC
    print bcolors.WARNING + "\n__________keep browsing into firefox and don't close terminal of proxychains__________ " + bcolors.ENDC
    browser = raw_input('Enter your browser name: ')
    browsin = "gnome-terminal -e 'bash -c \"proxychains {} www.google.com; exec bash\"'".format(browser)
    os.system(browsin)
    print bcolors.OKGREEN + "\n checking ip location" + bcolors.ENDC
    url = 'https://iplocation.com'
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    for tr in soup.find_all('tr'):
        print(tr.text)
   
def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input("lzfix > ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "\nERROR: Wrong Input"
		time.sleep(2)
		restart_program()    
    