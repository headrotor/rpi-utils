#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
shutdowndaemon.py
wait for pin 40 to be grounded, when it is, then do a clean shutdown
"""

#for blink(1) rgb indicator is in our path, if not don't use
blink1path = "/usr/local/sbin/blink1-tool"

# gpio pin to use as switch, see here for pinout
# http://www.raspberry-projects.com/pi/pi-hardware/raspberry-pi-2-model-b/rpi2-model-b-io-pins
# default is pin 40 (on B+ it's the end of connector near USB across from ground) in GPIO.BOARD mode
gpio_pin = 40 

import time
import RPi.GPIO as GPIO
from subprocess import call
from subprocess import Popen

# Set to True for debug output to log file
verbose = False
# set to True for dry run test (don't actually shut down :)
test = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# see if blink1-tool for blink(1) rgb indicator is in our path
import os.path
if os.path.isfile(blink1path):
    blink = True
    call(['sudo', blink1path, '--on', '-q'])
else:
    print "no blink(1) found"
    blink = False


# instead of being smart about it, just exit and log...
if GPIO.input(40) == 0:
    print "oops, trying to start up with offswitch off!"
    res = Popen(['sudo', blink1path,'--magenta','--blink', '60', '-q', '&'])
    exit(0)

blinkflag = True

while True:
    if GPIO.input(40) == 0:
        if verbose:
            print "trying to shut down..."
        if blink: #go red to show we are shutting down
            Popen(['sudo', blink1path,'--red','--blink', '60', '-q', '&'])
            # try a clean shutdown
        print "controlled shutdown at " + time.asctime()
        if test:
            print("would be shutting down here...")
        else: # for reals
            result = call(['sudo', '/sbin/shutdown', '--poweroff',  'now'])
            print result
        exit(0)
    else:
        time.sleep(0.5)
        if blink: #blink green to show daemon is running
            if blinkflag:
                blinkflag = False
                call(['sudo', blink1path, '--green', '-q'])
            else:
                blinkflag = True
                call(['sudo', blink1path,'--off', '-q'])
        if verbose:
            print "waiting..."
