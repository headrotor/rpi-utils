#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
shutdowndaemon.py
wait for pin 40 to be grounded, when it is, then do a clean shutdown
"""

import time
import RPi.GPIO as GPIO
from subprocess import call 

# Set to True for debug
verbose = True
while True:
#print str(GPIO.input(40))
    if GPIO.input(40) == 0:
        if verbose:
            print "trying to shut down..."
        # try a clean shutdown
        result = call(['sudo', '/sbin/shutdown', '--poweroff',  'now'])
        print result
        exit(0)
    else:
        time.sleep(0.1)
        if verbose:
            print "waiting..."
