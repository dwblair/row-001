import serial
import time
import glob
import numpy as np
baudrate=9600
ports=glob.glob("/dev/ttyACM*")
port=ports[-1]
port="/dev/ttyACM1"
print(port)
read_interval_secs=60
EXPECTED_NUM_PARAMS = 1

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
    resp=ser.readline().strip()
    params=resp.split(',')
    num_params=len(params)
    if num_params == EXPECTED_NUM_PARAMS:
        if check_params(params)==True:
            print(params)
            conductivity=params[0] #C
            print("conductivity="+conductivity)
            print("time="+str(time.time()))
            myfile = open("conductivity.tsv","a")
#            myfile.write(str(time.time())+'\t'+temperature+'\t'+pressure+'\t'+depth+'\n')
            myfile.write(str(time.time())+'\t'+conductivity+'\n')
            myfile.flush()
            myfile.close()
    
# print(len(resp))
#    params=[resp.strip() for x in resp.split(',')]
#    print(params)
    time.sleep(read_interval_secs)
   

