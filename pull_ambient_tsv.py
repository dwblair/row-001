import serial
import time
import glob
import numpy as np
baudrate=9600
ports=glob.glob("/dev/ttyACM*")
port=ports[-1]
print(port)
read_interval_secs=60
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
    resp=ser.readline().strip()
    params=resp.split(',')
    num_params=len(params)
    if num_params == EXPECTED_NUM_PARAMS:
        if check_params(params)==True:
            print(params)
            temperature=params[0] #C
            pressure=params[1] #mbar
            print("temp="+temperature)
            print("time="+str(time.time()))
            myfile = open("temp_ambient.tsv","a")
#            myfile.write(str(time.time())+'\t'+temperature+'\t'+pressure+'\t'+depth+'\n')
            myfile.write(str(time.time())+'\t'+temperature+'\n')
            myfile.flush()
            myfile.close()
            myfile = open("pressure_ambient.tsv","a")
#          myfile.write(str(time.time())+'\t'+temperature+'\t'+pressure+'\t'+depth+'\n')
            myfile.write(str(time.time())+'\t'+pressure+'\n')
            myfile.flush()
            myfile.close()
    
# print(len(resp))
#    params=[resp.strip() for x in resp.split(',')]
#    print(params)
    time.sleep(read_interval_secs)
   

