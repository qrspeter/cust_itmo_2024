import serial
import time
ser = serial.Serial('COM3')  # open serial port
print(ser.name)
k=0         
while k<5:
    ser.write(b'1')
    print('1')
    time.sleep(3)
    k+=1
    ser.write(b'0')
    print('0')
    time.sleep(3)
    
ser.close()             