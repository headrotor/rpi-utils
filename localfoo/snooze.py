#!/usr/bin/python3
# wait for an hour then stop mpd
# (if not playing, start play)
import os, sys
from subprocess import call, check_output
import time

# uses mpd2 for python 3 compat
# for python 3: sudo pip3 install python-mpd
# command ref http://pythonhosted.org/python-mpd2/topics/commands.html
from mpd import MPDClient, CommandError

def init_mpd(host='localhost'):
    client = MPDClient()               # create client object
    client.timeout = 10                # network timeout in secs (floats allow
    client.idletimeout = None          # timeout for idle is handled seperately
    client.connect(host, 6600)  # connect to localhost:6600
    return client

if __name__ == "__main__":

    client = init_mpd()
    # are we playing or streaming? 
    result = client.status();
    if result['state'] == 'play':
        sys.stdout.write('snooze.py: snoozing in 3600\n')
        time.sleep(3600)
        client.stop()
        sys.stdout.write('snooze.py: snoozed\n')
    else:
        client.play()
        sys.stdout.write('snooze.py: playing\n') 

    
