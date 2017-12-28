import serial
import time
import glob
import numpy as np
import json
baudrate=9600
ports=glob.glob("/dev/ttyACM*")
port=ports[-1]
port="/dev/ttyACM1"
print(port)
read_interval_secs=3
EXPECTED_NUM_PARAMS = 2


def is_number(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def check_params(params):
    all_nums=True
    for param in params:
        if (is_number(param)==False):
            all_nums=False
    return all_nums
    
while True:
    ser=serial.Serial(port,baudrate=baudrate)
    ser.reset_input_buffer()
    line=ser.readline()
    print(line)
    print(line.split('\t'))
    packet=line.split('\t')[1]
    print(packet)
    results=json.loads(packet)
    print(results)
    temp=results["data"]["temp"]
    conductivity_adc=results["data"]["conductivity"]
    print(temp,conductivity_adc)
    time.sleep(read_interval_secs)
   

