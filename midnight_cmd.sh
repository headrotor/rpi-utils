#!/bin/bash
# run this at midnight: crontab -e
# 0 0 * * *  ~/midnight_cmd.sh  >> ~/cronlog.txt 2>&1


# turn off lights at midnight. Hit them a couple times because UDP
cd /home/jtf/gith/m5stack-display
for (( c=1; c<=10; c++ ))
do  
   /home/jtf/anaconda3/bin/python3 /home/jtf/gith/m5stack-display/osc-switcher.py 2 off
   sleep 2
done

if [ -t 1 ] ; then
    echo "No sleep" 
else
    sleep 3600
fi    

for (( c=1; c<=10; c++ ))
do  
   /home/jtf/anaconda3/bin/python3 /home/jtf/gith/m5stack-display/osc-switcher.py 1 off
   sleep 2
done

if [ -t 1 ] ; then
    echo "No sleep" 
else
    sleep 3600
fi    

for (( c=1; c<=10; c++ ))
do  
   /home/jtf/anaconda3/bin/python3 /home/jtf/gith/m5stack-display/osc-switcher.py 3 off
   sleep 2
done
