import serial
import time
import glob
import numpy as np
baudrate=9600
num_params=4
ports=glob.glob("/dev/ttyUSB*")
print(ports)
ports=glob.glob("/dev/ttyACM*")
print(ports)
