#!/usr/bin/python
import sys
from scapy.all import *
from subprocess import call, Popen
def arp_display(pkt):
  if pkt.haslayer(ARP):
    if pkt[ARP].op == 1: #who-has (request)
      #print "found arp 1 hwsrc " + pkt[ARP].hwsrc + " psrc " + pkt[ARP].psrc 
      if pkt[ARP].hwsrc == '74:75:48:26:b2:ac': # ARP Prob
        sys.stdout.write('Dash ac detected\n')
        Popen(['/usr/bin/python3','/home/pi/gith/rpi-utils/localfoo/snooze.py'])
        call(['date'])
      elif pkt[ARP].hwsrc == '74:c2:46:08:7c:d5':
        sys.stdout.write('print "Dash d5 detected\n')
        Popen(['/bin/bash', '/home/pi/top_curtains.sh'])
        call(['date'])
      elif pkt[ARP].hwsrc == '10:ae:60:ef:15:49':
        sys.stdout.write('Dash 49 detected')
        call(['mpc','toggle'])
        call(['date'])

        
#print sniff(prn=arp_display, filter="arp", store=0, count=50)
# run forever
print sniff(prn=arp_display, filter="arp", store=0)
