#!usr/bin/env python

import scapy.all as scapy
import optparse
import pyfiglet
import subprocess

def requirements():

    #subprocess(['pip3', 'install', 'scapy'])
    #subprocess(['pip3', 'install', 'optparse'])
    #subprocess(['pip3', 'install', 'pyfiglet'])

    subprocess.check_output(['pip3', 'install', 'scapy'])
    #subprocess.check_output(['pip3', 'install', 'optparse'])
    subprocess.check_output(['pip3', 'install', 'pyfiglet'])

def get_arguements():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", help="IP Address or range of IP Addresses", dest="ip")
    parser.add_option("-d", "--dependences", help="To install required dependences like python modules", dest="dependences")
    (options, arguements) = parser.parse_args()

    if not options.ip:
        parser.error("[-] Please provide an IP Address or IP Address range")
    if options.ip:
        return options

def scan(ip):

    arp_packet = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_packet

    answer = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP Address \t\t\t MAC Address \n-------------------------------------------------")

    for element in answer:
        print(element[1].psrc + "\t\t\t" + element[1].hwsrc)


intro = pyfiglet.figlet_format("IP Scanner", font="standard")
print(intro)
print("------> IP Scanner V 1.1 by Aditya Patil <-------")
print("-------------------------------------------------")
print("[+] If the program gives any error, consider using\n -d 0 or --dependences 0 to download required python modules")

options = get_arguements()

if options.dependences == "0":

    print("[+] Please wait, installing the required dependences")
    requirements()

print("-------------------------------------------------")

ip = options.ip
scan(ip)

print("-------------------------------------------------")



