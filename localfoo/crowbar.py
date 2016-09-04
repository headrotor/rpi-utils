def parse_aticonfig(s):
    for line in s.split('\n'):
        l = line.strip()
        if l.startswith('Sensor 0: Temperature - '):
            return l.split('Sensor 0: Temperature - ')[1].split()[0]

    return None


def get_aticonfig_output():
    s = subprocess.check_output(["aticonfig", "--adapter=0", "--od-gettemperature"])

    return s
