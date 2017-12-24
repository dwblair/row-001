import serial
import time
import glob
import numpy as np
baudrate=9600
num_params=4
ports=glob.glob("/dev/ttyUSB*")
port=ports[-1]
print(port)
read_interval_secs=60


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
    if num_params == 4:
        if check_params(params)==True:
            print(params)
            fluidDensity=params[0] #kg/m^3
            pressure=params[1] #mbar
            temperature=params[2] #C
            depth=params[3] #meters
            print("temp="+temperature)
            print("time="+str(time.time()))
            myfile = open("temp.tsv","a")
#            myfile.write(str(time.time())+'\t'+temperature+'\t'+pressure+'\t'+depth+'\n')
            myfile.write(str(time.time())+'\t'+temperature+'\n')
            myfile.flush()
            myfile.close()
            myfile = open("depth.tsv","a")
#          myfile.write(str(time.time())+'\t'+temperature+'\t'+pressure+'\t'+depth+'\n')
            myfile.write(str(time.time())+'\t'+depth+'\n')
            myfile.flush()
            myfile.close()
            myfile = open("pressure.tsv","a")
#          myfile.write(str(time.time())+'\t'+temperature+'\t'+pressure+'\t'+depth+'\n')
            myfile.write(str(time.time())+'\t'+pressure+'\n')
            myfile.flush()
            myfile.close()
#        else:
#            print("Bad params:")
#            print(resp)
#            print(params)    
    
# print(len(resp))
#    params=[resp.strip() for x in resp.split(',')]
#    print(params)
    time.sleep(read_interval_secs)
   

