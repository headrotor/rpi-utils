#!/bin/bash
killall mpd-control.py
#sudo /home/pi/gith/pidp-python/mpd-control.py > /var/log/mpd-control.log 2>&1 &
sudo /home/pi/gith/pidp-python/mpd-control.py > /dev/null 2> /var/log/mpd-err.log &
killall dash-daemon.py
sudo /home/pi/hack/dash-daemon.py > /var/log/dash-daemon.log 2>&1 &
#sudo /home/pi/hack/dash-daemon.py > /dev/null 2>&1 &
