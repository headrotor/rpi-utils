# for testing crowbar, simulate aticonfig
import subprocess
import time
import datetime



crowbar_temp = 72.0

def parse_aticonfig(s, gpu):
    for line in s.splitlines():
        l = line.strip()
        startline = 'Sensor {}: Temperature - '.format(gpu)
        if l.startswith(startline):
            return l.split(startline)[1].split()[0].strip()

    return None


def get_ati_temp(GPU):
    adapter = "--adapter={:d}".format(int(GPU))
    s = subprocess.check_output(["python", "aticonfig.py", adapter, "--od-gettemperature"])
    
    return s

def crowbar(GPU, temp):
    """ call this when it's time to crowbar"""
    s = subprocess.check_output(["sudo", "killall", "ethminer"])
    now = datetime.datetime.now()
    nowstr = str(now)[:19]
    print("GPU {} temp {} crowbar at time {}".format(GPU, temp, nowstr))
    print s

if __name__ == "__main__":
    GPUs = [0, 1, 2, 3]
    for gpu in GPUs:
        s = get_ati_temp(gpu)
        temp = float(parse_aticonfig(s, str(gpu)))
        print("Adaptor:{} temp:{}".format(gpu,temp))
        if temp > crowbar_temp:
            crowbar(gpu, temp)
