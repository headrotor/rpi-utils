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

def rmfile(fn):
    try:
        os.remove(fn)
    except OSError:
        pass

def touchfile(fn):
    with open(fn, 'w+') as f:
        f.write('snoozin')

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("usage: snooze <n>  where n is minutes before mute")
        exit(0)

    snooze_time = 60*float(sys.argv[1])
    statusf = '/home/pi/.snooze'
    client = init_mpd()

    # first, are we already waiting to snooze?
    if os.path.isfile(statusf):
        sys.stdout.write('already snoozin, stopped\n')
        #stop snooze and delete snoozefile
        client.stop()
        rmfile(statusf)
    else:
        # are we playing or streaming? 
        result = client.status();
        if result['state'] == 'play':
            # client tends to timeout during sleep, so stop it and reopen
            client.close()
            client.disconnect()
            then = time.time() + snooze_time
            sys.stdout.write('snooze.py: snoozing until {0:f}\n'.format(
                then))
            sys.stdout.flush()
            touchfile(statusf)
            while time.time() < then:
                sys.stdout.write('now at {0:f}\n'.format(time.time() - then))
                sys.stdout.flush()
                time.sleep(30)
            client = init_mpd()
            client.stop()
            rmfile(statusf)
            sys.stdout.write('snooze.py: snoozed\n')
        else:
            client.play()
            sys.stdout.write('snooze.py: playing\n') 

    
