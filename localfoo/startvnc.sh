#!/bin/bash
killall Xorg
nohup sudo startx > /var/log/startx.log 2>&1 &
sleep 2
killall Xtightvnc
rm /tmp/.X*-lock
nohup vncserver :1 -geometry 1024x728 -depth 24 > /var/log/vnc.log 2>&1 &
#sudo x11vnc -usepw 
