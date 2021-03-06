#!/bin/bash
# source: https://www.raspberrypi.org/forums/viewtopic.php?f=31&t=141082
# thanks rpidom!
while true
do
  cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)
  cpuTemp1=$(($cpuTemp0/1000))
  cpuTemp2=$(($cpuTemp0/100))
  cpuTempM=$(($cpuTemp2 %$cpuTemp1))
  clear
  echo "CPU temp=$cpuTemp1.$cpuTempM'C"
  echo "GPU $(/opt/vc/bin/vcgencmd measure_temp)"
  echo "clk $(/opt/vc/bin/vcgencmd measure_clock arm)"
  echo "~turbo: $(/usr/bin/gpio -g read 35)"
  sleep 1
done
