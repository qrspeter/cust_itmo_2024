# https://forum.arduino.cc/t/using-python-to-read-and-process-serial-data-from-arduino/1059079

import serial


def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:
        #data = ser.readline().decode().strip()
        data = ser.read ()
        if data:
            print(data)


if __name__ == '__main__':

    readserial('COM4', 9600)