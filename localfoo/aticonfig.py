# for testing crowbar, simulate aticonfig
import sys

outstr = """Adapter {0} - AMD Radeon HD 6900 Series
Sensor {0}: Temperature - {1}.00 C"""

if __name__ == "__main__":
    argstr = sys.argv[1]
    gpu = argstr[-1]
    sys.stdout.write(outstr.format(str(gpu), str(70 + int(gpu))))
