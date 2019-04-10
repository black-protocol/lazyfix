## lazyfix.py - Lazyfix v2.8
# -*- coding: utf-8 -*-
##
import os
import sys
from time import sleep as timeout
from core.lzmcore import *
from core.tor import *

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'

def main():
    banner()
        print " [01] FIX KALI ERROR" 
        print " [02] SOURCES.LIST"
        print " [03] MODE ANONYMOUS"
        print " [04] CHECK WEBSITE SQL VULNERABILITY"
        print bcolors.BOLD + "\n   [10] Exit the fixkali\n" + bcolors.ENDC
	lazyfix = raw_input("wolf > ")
  
	if lazyfix == "1" or lazyfix == "01":
		print bcolors.OKGREEN + "    [01] vpn" + bcolors.ENDC
		print bcolors.OKGREEN + "    [02] tor"  + bcolors.ENDC
  	        print bcolors.OKGREEN + "    [03] gpg_error" + bcolors.ENDC
	        print bcolors.OKGREEN + "    [04] audio_error" + bcolors.ENDC
		print bcolors.OKGREEN + "    [05] WIFI_PROBLEM_NO_WIFI_SHOWN" + bcolors.ENDC
		print bcolors.OKGREEN + "    [06] Wifi_Adapter_Not_Detecting" + bcolors.ENDC
		print bcolors.OKGREEN + "    [07] Administrator_Directory_Lock_Problem" + bcolors.ENDC
		print bcolors.OKGREEN + "    [08] Unable_to_Locate_Package_kali1.0" + bcolors.ENDC
		print bcolors.OKGREEN + "    [09] Unable_to_Locate_Package_kali2.0" + bcolors.ENDC
	        print bcolors.BOLD + "\n    [00] Back to main menu \n" + bcolors.ENDC
		fixkali = raw_input("wolf > ")
		
		if fixkali == "01" or fixkali == "1":
			vpn()
		elif fixkali == "02" or fixkali == "2":
			tor()
                elif fixkali == "03" or fixkali == "3":
			gpg_error()  
		elif fixkali == "04" or fixkali == "4":
			audio_error()	
		elif fixkali == "05" or fixkali == "5":
			WIFI_PROBLEM_NO_WIFI_SHOWN()
		elif fixkali == "06" or fixkali == "6":
			Wifi_Adapter_Not_Detecting()
		elif fixkali == "07" or fixkali == "7":
			Administrator_Directory_Lock_Problem()		
		elif fixkali == "08" or fixkali == "8":
			Unable_to_Locate_Package_kali1_0()
		elif fixkali == "09" or fixkali == "9":
			Unable_to_Locate_Package_kali2_0()	
		elif fixkali == "00" or fixkali == "0":
			restart_program()
			
		else:
			print bcolors.FAIL + "\nERROR: Wrong Input" + bcolors.ENDC
			timeout(2)
			restart_program()


        elif lazyfix == "2" or lazyfix == "02":
		print bcolors.OKGREEN + "\n    [01] sources_kali1" + bcolors.ENDC
		print bcolors.OKGREEN + "    [02] sources_kali2" + bcolors.ENDC
	        print bcolors.BOLD + "\n    [00] Back to main menu\n" + bcolors.ENDC
		sources = raw_input("wolf > ")
		
		if sources == "01" or sources == "1":
			sources_kali1()
		elif sources == "02" or sources == "2":
			sources_kali2()
		elif sources == "00" or sources == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()

        elif lazyfix == "3" or lazyfix == "03":
		print bcolors.OKGREEN + "      [*] first_step" + bcolors.ENDC
                print bcolors.OKGREEN + "      [**] second_step" + bcolors.ENDC
		print bcolors.OKGREEN + "      [***] third_step" + bcolors.ENDC
	        print bcolors.BOLD + "\n    [00] Back to main menu\n" + bcolors.ENDC
		anonymous = raw_input("wolf > ")
		
		if anonymous == "[*]" or anonymous == "*":
			first_step()
		elif anonymous == "[**]" or anonymous == "**":
			second_step()
                elif anonymous ==  "[***]" or anonymous == "***":
                        third_step()
                elif anonymous == "00" or anonymous == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()

        if lazyfix == "4" or lazyfix == "04":
		    sql_injection()
		
		
	elif lazyfix == "10":
		sys.exit()
	
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()
