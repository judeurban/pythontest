#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    idx = 0
    while True:
        sendString = "Hello from Raspberry Pi! " + idx + "\n"
        ser.write(sendString.encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        idx += 1
        time.sleep(1)