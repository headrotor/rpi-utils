#!/bin/bash
killall mpd-control.py

sudo /home/pi/gith/pidp-python/mpd-control.py > /dev/null 2> /var/log/mpd-err.log &
sleep 3
killall dash-poll-daemon.py
sudo /home/pi/gith/rpi-utils/localfoo/dash-poll-daemon.py > /var/log/dash-daemon.log 2>&1 &

