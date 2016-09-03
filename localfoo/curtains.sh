#/bin/bash
CURTAIN_STATUS=$(/usr/local/bin/wemo switch "$1" status)
#echo $CURTAIN_STATUS
if [ "$CURTAIN_STATUS" = 1 ]; then
    #echo on  so blink off
    /usr/local/bin/wemo switch "$1" off
    sleep 1
fi
/usr/local/bin/wemo switch "$1" on
sleep 35
/usr/local/bin/wemo switch "$1" off
exit 0
