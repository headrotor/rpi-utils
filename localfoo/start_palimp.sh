#!/bin/bash
# on_startup.sh : run by /etc/rc.local on startup
sudo killall -SIGUSR1 palimp
sudo killall -SIGUSR1 faceball
/home/pi/openFrameworks/apps/ofx/palimp/bin/palimp >> /var/log/palimp.log 2>&1 &

# startup anything else you want here
