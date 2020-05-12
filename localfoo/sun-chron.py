
# python cron job to do things at sunrise and sunset using 'at'
# run daily from crontab, e.g.


import sys
import time
import datetime
from astral import Astral
import subprocess



if __name__ == '__main__':


    city_name = "San Francisco"
    a = Astral()
    #a.solar_depression = 'civil'
    #a.solar_depression = 'nautical'
    # three degrees below horizon, so just a little after sunset
    a.solar_depression = 2.0

    city = a[city_name]

    print('Information for %s/%s\n' % (city_name, city.region))

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    print("tomorrow is {} {} {}".format(tomorrow.year,
                                        tomorrow.month,
                                        tomorrow.day))
    y, m, d = tomorrow.year, tomorrow.month, tomorrow.day
    sun = city.sun(date=datetime.date(y, m, d), local=True)
    print('Sunrise:  %s' % str(sun['sunrise']))
    print('Sunset:  %s' % str(sun['sunset']))
    print('Dusk:  %s' % str(sun['dusk']))


    # at defaults to tomorrow
    #print('Sunset:  {} {}' % sun[sunset].hour, sun.minute)
    print('at -f ~/sunset_cmd.sh {:02d}:{:02d}'.format(sun['dusk'].hour,sun['dusk'].minute))
    print('at -f ~/sunrise_cmd.sh {:02d}:{:02d}'.format(sun['sunrise'].hour,sun['sunrise'].minute))
    


    sunrise_cmd = ['at', '-f', '/home/jtf/sunrise_cmd.sh']
    sunrise_cmd.append('{:02d}:{:02d}'.format(sun['sunrise'].hour,sun['sunrise'].minute))
    subprocess.run(sunrise_cmd)

    sunset_cmd = ['at', '-f', '/home/jtf/sunset_cmd.sh']
    sunset_cmd.append('{:02d}:{:02d}'.format(sun['dusk'].hour,sun['dusk'].minute))
    subprocess.run(sunset_cmd)
