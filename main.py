# main.py: Asks for a string and sends it to a serial

import toBraille as tm
import serial

# initialization of the serial
ser = serial.Serial('COM3', 9600)

# infinite loop asking user for a string
while True:
    str = input("Enter a string: ")
    temp = tm.stringToBinary(str)

    # sends string of 1s and 0s to serial one by one
    # can later change to send a base 8 value instead of binary to decrease amount sent
    for x in range(len(temp)): 
        num = temp[x]
        ser.write(num.encode())

