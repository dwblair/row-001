import serial
import time
import glob
import numpy as np
baudrate=9600

PORT_ROW="/dev/ttyUSB0"
PORT_AMBIENT="/dev/ttyACM0"
PORT_CONDUCT="/dev/ttyACM1"

read_interval_secs=60

ROW_NUM_PARAMS = 4
AMBIENT_NUM_PARAMS=2
CONDUCT_NUM_PARAMS=2

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

def pull_params(port,expected_num_params):
    print("reading "+str(expected_num_params)+" params from port "+port+":")
    ser=serial.Serial(port,baudrate=baudrate)
    ser.reset_input_buffer()
    resp=ser.readline().strip()
    params=resp.split(',')
    num_params=len(params)
    if (num_params == expected_num_params):
        if check_params(params)==True:
            return params
        else:
            return "error"
    ser.close()

while True:
    timestamp=time.time() #same timestamp for all
    print('----------------------------')
    print('timestamp='+str(timestamp))

    failed=False
    
    # get row sensor
    params=pull_params(PORT_ROW,ROW_NUM_PARAMS)
    if (params!=None):
        print(params)
        fluidDensity=params[0] #kg/m^3
        pressure_row=params[1] #mbar
        temperature=params[2] #C
        depth_row=params[3] #meters
        myfile = open("temp.tsv","a")
        myfile.write(str(timestamp)+'\t'+temperature+'\n')
        myfile.flush()
        myfile.close()
        myfile = open("pressure.tsv","a")
        myfile.write(str(timestamp)+'\t'+pressure_row+'\n')
        myfile.flush()
        myfile.close()
        myfile = open("depth.tsv","a")
        myfile.write(str(timestamp)+'\t'+depth_row+'\n')
        myfile.flush()
        myfile.close()
    else:
        failed=True
        
        
    # get ambient sensor
    params=pull_params(PORT_AMBIENT,AMBIENT_NUM_PARAMS)
    if (params!=None):
        print(params)
        temp_ambient=params[0] #C
        pressure_ambient=params[1] #mbarmyfile = open("temp_ambient.tsv","a")
        myfile = open("temp_ambient.tsv","a")
        myfile.write(str(timestamp)+'\t'+temp_ambient+'\n')
        myfile.flush()
        myfile.close()
        myfile = open("pressure_ambient.tsv","a")
        myfile.write(str(timestamp)+'\t'+pressure_ambient+'\n')
        myfile.flush()
        myfile.close()
    else:
        failed=True
    # produce corrected pressure
    if failed==False:
        myfile=open("pressure_corrected.tsv","a")
        print('diagnostic:')
        print('pressure_row',pressure_row)
        print('pressure_ambient',pressure_ambient)
        pressure_corrected=str(float(pressure_row)-float(pressure_ambient))
        print("pressure_corrected="+pressure_corrected);
        myfile.write(str(timestamp)+'\t'+pressure_corrected+'\n')
        myfile.flush()
        myfile.close()
        
    # get conductivity_sensor
    params=pull_params(PORT_CONDUCT,CONDUCT_NUM_PARAMS)
    if (params!=None):
        print(params)
        conductivity=params[0] #C
        temperature=params[1]
        myfile = open("conductivity_adc.tsv","a")
        myfile.write(str(timestamp)+'\t'+conductivity+'\n')
        myfile.flush()
        myfile.close()
        myfile = open("conduct_temp.tsv","a")
        myfile.write(str(timestamp)+'\t'+temperature+'\n')
        myfile.flush()
        myfile.close()
        
        t=float(temperature)
        adc=float(conductivity)
        c=(adc-1956.4)/0.154
        print("conductivity="+str(c))
        sp_c=c/(1+0.02*(t-25))
        print("specific_conductivity="+str(sp_c))
        myfile = open("conductivity_specific.tsv","a")
        myfile.write(str(timestamp)+'\t'+str(sp_c)+'\n')
        myfile.flush()
        myfile.close()
        
        
    time.sleep(read_interval_secs)
