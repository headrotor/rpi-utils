#!/usr/bin/python
# scapy approach stopper working on some Jessie upgrade so ugly hack: poll the dash buttons using ping
#

#https://www.raspberrypi.org/forums/viewtopic.php?f=106&t=109621#p753241

import sys
from subprocess import call, Popen
import time
import os

# def arp_display(pkt):
#   if pkt.haslayer(ARP):
#     if pkt[ARP].op == 1: #who-has (request)
#       print "found arp 1 hwsrc " + pkt[ARP].hwsrc + " psrc " + pkt[ARP].psrc 
#       if pkt[ARP].hwsrc == '74:75:48:26:b2:ac': # ARP Prob
#         sys.stdout.write('Dash ac detected\n')
#         Popen(['/usr/bin/python3',
#                '/home/pi/gith/rpi-utils/localfoo/snooze.py',
#                '15'])
#         call(['date'])
#       elif pkt[ARP].hwsrc == '74:c2:46:08:7c:d5':
#         sys.stdout.write('print "Dash d5 detected\n')
#         Popen(['/bin/bash', '/home/pi/top_curtains.sh'])
#         call(['date'])
#       elif pkt[ARP].hwsrc == '10:ae:60:ef:15:49':
#         sys.stdout.write('Dash 49 detected')
#         call(['mpc','toggle'])
#         call(['date'])

        
#print sniff(prn=arp_display, filter="arp", store=0, count=50)
# run forever
#print sniff(prn=arp_display, filter="arp", store=0)



class Dashbutton(object):
    def __init__(self, name, IP):
        self.IP = IP
        self.name = name
        self.up = False
        self.command = []
        
    def isup(self):
        # Returns True if ping shows dash is up (has been pressed)
        response = os.system("ping -c 1 -W 1 -n " + self.IP + " > /dev/null 2>&1")
        if response == 0:
            return True
        return False

    def is_newly_up(self):
        # Returns True only once per button press
        if self.isup():
            if self.up is False:
                self.up = True
                return True
            else:
                self.up = True
                return False
        else:
            self.up = False
        return False

    def execute(self):
        #print str(self.command)
        Popen(self.command)
    
dashes = []

d = Dashbutton('snooze', '192.168.1.200')
d.command = ['/usr/bin/python3',
                 '/home/pi/gith/rpi-utils/localfoo/snooze.py',
                 '15']
dashes.append(d)

d = Dashbutton('top', '192.168.1.201')
d.command = ['/bin/bash', '/home/pi/top_curtains.sh']
dashes.append(d)

d = Dashbutton('door', '192.168.1.141')
d.command = ['mpc','toggle']
dashes.append(d)

while True:

    for dash in dashes:
        if dash.is_newly_up():
            print dash.name + ' was pressed'
            dash.execute()
            call(['date'])
        else:
            pass
            #print dash.name, 'is down!'
    time.sleep(1)
