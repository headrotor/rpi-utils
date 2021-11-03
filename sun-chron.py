#/home/jtf/anaconda3/bin/python
# python cron job to do things at sunrise and sunset using 'at'
# run daily from crontab, e.g.


import sys
import time
import datetime
from astral.sun import sun
from astral import LocationInfo
from astral.geocoder import database, lookup
import astral
import subprocess
import pytz



if __name__ == '__main__':



    
    #a.solar_depression = 'civil'
    #a.solar_depression = 'nautical'
    # degrees below horizon, so just a little after sunset
    sun.solar_depression = 1.0
    #sun.solar_depression = 0.0

    #city = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)
    city = lookup("San Francisco", database())

    print('Information for %s/%s\n' % (city.name, city.region))

    print((
        f"Information for {city.name}/{city.region}\n"
        f"Timezone: {city.timezone}\n"
        f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
    ))

    
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    print("tomorrow is {} {} {}".format(tomorrow.year,
                                        tomorrow.month,
                                        tomorrow.day))
    y, m, d = tomorrow.year, tomorrow.month, tomorrow.day
    s  = sun(city.observer, date=datetime.date(y, m, d),
             tzinfo=pytz.timezone(city.timezone),
             dawn_dusk_depression=sun.solar_depression)
    print('Sunrise:  %s' % str(s['sunrise']))
    print('Sunset:  %s' % str(s['sunset']))
    print('Dusk:  %s' % str(s['dusk']))

    
    # at defaults to tomorrow
    #print('Sunset:  {} {}' % sun[sunset].hour, sun.minute)
    print('at -f ~/bin/sunset_cmd.sh {:02d}:{:02d}'.format(s['dusk'].hour,s['dusk'].minute))
    print('at -f ~/bin/sunrise_cmd.sh {:02d}:{:02d}'.format(s['sunrise'].hour,s['sunrise'].minute))
    

    sunrise_cmd = ['at', '-f', '/home/jtf/bin/sunrise_cmd.sh']
    sunrise_cmd.append('{:02d}:{:02d}'.format(s['sunrise'].hour,s['sunrise'].minute))
    subprocess.run(sunrise_cmd)

    sunset_cmd = ['at', '-f', '/home/jtf/bin/sunset_cmd.sh']
    sunset_cmd.append('{:02d}:{:02d}'.format(s['dusk'].hour,s['dusk'].minute))
    subprocess.run(sunset_cmd)
