## lzmfix.py - useful module of Lazyfix
# -*- coding: utf-8 -*-
import os
import sys
import time
import requests

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'

lazyfix_banner = """
▒█░░░ ░█▀▀█ ▒█▀▀▀█ ▒█░░▒█ ▒█▀▀▀ ▀█▀ ▀▄▒▄▀ 
▒█░░░ ▒█▄▄█ ░▄▄▄▀▀ ▒█▄▄▄█ ▒█▀▀▀ ▒█░ ░▒█░░ 
▒█▄▄█ ▒█░▒█ ▒█▄▄▄█ ░░▒█░░ ▒█░░░ ▄█▄ ▄▀▒▀▄    
*/--------------------------------------/*
*-**********SCRIPT BY WOLF**************-*
*- website: https://omegeng.blogspot.com-*                           
*/--------------------------------------/*                            
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the Lazyfix
"""
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

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

def banner():
	print lazyfix_banner

def vpn():
	print '\n###### Installing VPN(for kali)'
	os.system('apt update && apt upgrade')
	os.system('apt-get install network-manager-openvpn-gnome')
	os.system('apt-get install network-manager-pptp')
	os.system('apt-get install network-manager-pptp-gnome')
        os.system('apt-get install network-manager-strongswan')
        os.system('apt-get install network-manager-vpnc')
        os.system('apt-get install network-manager-vpnc-gnome')
        os.system('/etc/init.d/network-manager restart')
	print bcolors.OKGREEN + "###### Done" + bcolors.ENDC
	print bcolors.OKGREEN + "###### your vpn ready to start." + bcolors.ENDC
	backtomenu_option()

def tor():
	print bcolors.OKGREEN + "\n###### Installing TOR" + bcolors.ENDC
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('apt-get install tor')
	print bcolors.OKGREEN + "###### Done" + bcolors.ENDC
        print bcolors.OKGREEN + "###### type 'tor' to start." + bcolors.ENDC
	backtomenu_option()

def gpg_error():
	print bcolors.OKGREEN + "\n###### Installing gpg_error" + bcolors.ENDC
	os.system('apt update && apt upgrade')
	os.system('apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6')
        os.system('apt-get update')
	print bcolors.OKGREEN + "###### Done" + bcolors.ENDC
        print bcolors.OKGREEN + "###### your problem solved." + bcolors.ENDC
	backtomenu_option()

def sources_kali1():
	print bcolors.OKGREEN + "\n######  your sources are update try type 'apt-get update'."+ bcolors.ENDC 
        file = open('/etc/apt/sources.list', 'w')
        file.write('deb http://old.kali.org/kali moto main non-free contrib\n')
        file.write('# For source package access, uncomment the following line\n')
        file.write('# deb-src http://old.kali.org/kali moto main non-free contrib\n')
        file.close()
	backtomenu_option()

def sources_kali2():
	print bcolors.OKGREEN + "\n######  your sources are update try type 'apt-get update'."+ bcolors.ENDC 
	os.system('cd /etc/apt')
        file = open('/etc/apt/sources.list', 'w')
        file.write('deb http://http.kali.org/kali kali-rolling main non-free contrib\n')
        file.write('deb-src http://http.kali.org/kali kali-rolling main non-free contrib\n')
        file.close()
	backtomenu_option()

def audio_error():
	print bcolors.OKGREEN + "\n   fixing error\n" + bcolors.ENDC
        os.system('pulseaudio -D')
	os.system('apt-get update && apt-get upgrade')
        print bcolors.OKGREEN + "\n   your problem fixed check audio option\n" + bcolors.ENDC
	backtomenu_option()
	
def WIFI_PROBLEM_NO_WIFI_SHOWN():
	print bcolors.OKGREEN + "\n   fixing WIFI PROBLEM (NO WIFI SHOWN/NOT SHOWING UP)\n" + bcolors.ENDC
        os.system('service network-manager restart')
	os.system('nmcli networking on')
	os.system('apt-get update && apt-get upgrade')
        print bcolors.OKGREEN + "\n   your problem fixed check WIFI option\n" + bcolors.ENDC
	backtomenu_option()	

def Wifi_Adapter_Not_Detecting():
	print bcolors.OKGREEN + "\n   fixing Wifi Adapter (Not Detecting) \n" + bcolors.ENDC
        os.system('cd ~/Desktop')
	os.system('apt-get install wget')
	os.system('wget http://linuxwireless.org/download/compat-wireless-2.6/compat-wireless-2010-06-26-p.tar.bz2')
	os.system('tar -jxvf compat-wireless-2010-06-26-p.tar.bz2')
	os.system('ls')
	os.system('cd compat-*')
	os.system('ls')
	os.system('make unload')
	os.system('make load')
	os.system('clear')
        print bcolors.OKGREEN + "\n   your problem fixed check WIFI option or type 'ifconfig'\n" + bcolors.ENDC
	backtomenu_option()	
	
def Administrator_Directory_Lock_Problem():
	print bcolors.OKGREEN + "\n   fixing Administrator Directory Lock (/var/lib/apt/lists/lock) \n" + bcolors.ENDC
        os.system('sudo rm /var/lib/dpkg/lock')
	os.system('sudo dpkg --configure -a')
	os.system('apt-get update')
	print bcolors.OKGREEN + "\n   your problem fixed\n" + bcolors.ENDC
	backtomenu_option()
	
def Unable_to_Locate_Package_kali1_0():
        print bcolors.OKBLUE + "\n######  your problem fixed " + bcolors.ENDC
        print bcolors.OKGREEN + "\n######  turn on connection and type 'apt-get update' " + bcolors.ENDC
        os.system('cd /etc/apt')
        file = open('/etc/apt/sources.list', 'w')
        file.write('deb http://old.kali.org/kali moto main non-free contrib\n')
        file.write('# For source package access, uncomment the following line\n')
        file.write('# deb-src http://old.kali.org/kali moto main non-free contrib\n')
        file.close()
        backtomenu_option()

def Unable_to_Locate_Package_kali2_0():
        print bcolors.OKGREEN + "\n######  turn on connection for get update " + bcolors.ENDC
        os.system('cd /etc/apt')
        file = open('/etc/apt/sources.list', 'w')
        file.write('deb http://http.kali.org/kali kali-rolling main non-free contrib\n')
        file.write('deb-src http://http.kali.org/kali kali-rolling main non-free contrib\n')
        file.close()
        backtomenu_option()

def first_step():		
        print bcolors.OKGREEN + "\n######  install requirements for mode anonymous " + bcolors.ENDC
        os.system('cd /etc/')
	time.sleep(2)
	os.remove('/etc/proxychains.conf')
        os.system('apt-get install tor')
        os.system('service tor start')
        os.system('/etc/init.d/tor start')
        backtomenu_option()

def second_step():
        print bcolors.OKGREEN + "\n######  start change ip and change mac address for you  " + bcolors.ENDC
        os.system('macchanger -s eth0')
	os.system('cd /root/Desktop/lazyfix2.9/file/')
        time.sleep(2)
        os.system('cp /root/Desktop/lazyfix2.9/file/proxychains.conf /etc/')
        os.system('chmod +x tor-buddy.sh')
        time.sleep(2)
        os.system("gnome-terminal -e 'bash -c \"./tor-buddy.sh; exec bash\"'")
	print bcolors.OKGREEN + "\n ###done " + bcolors.ENDC
        backtomenu_option()
        
def sql_injection():
        print bcolors.OKGREEN + "\n######  put your website with this sympol ' in end of url  " + bcolors.ENDC
        time.sleep(4)
        url = raw_input('Enter your website: ')
        r = requests.get(url)
        if 'You have an error in your SQL' in r.text:
          print bcolors.OKGREEN + "\n######  your website is vulnerability " + bcolors.ENDC
        else:
          print bcolors.FAIL + "\n###### your website is not vulnerability " + bcolors.ENDC
		
