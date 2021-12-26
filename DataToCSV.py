"""
DataToCSV.py : is made to read and parse the data from the serial.
"""

# Importing serial = So that we can play with the USB data
# Importing CSV to be able to read and write CSV files
# Importing datetime for timestamps on the data
# Importing pandas for data analysis
import serial
import csv
from datetime import datetime
import time
import pandas as pd

def SaveDatatoCSV():
    # Configuration for serial port
    # COM4 is a specific communication-port (data transmission in serial port)
    # Baudrate optimized for Arduino configuration
    serialPort = serial.Serial(port="COM4", baudrate=115200,
                               bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    # Settings for writing data

    # f = open('data.csv', 'w', newline='', encoding='utf-8')

    startTime = time.time();
    totalSeconds = 30;

    # While loop, including parsing and sorting the given data into a CSV.file
    # Because we want to write and read sequences into CSV, we use the DictWriter & DictReader
    # serialPort is the USB port, where the data is transferred and gathered into this program, and then decoded
    with open("data.csv", "w") as file:
        # fieldnames=['PACKET', 'CHAN', 'RSSI', 'ADDR1', 'ADDR2', 'ADDR3']
        fieldnames=['Timestamp', 'ID']
        dw = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
        dw.writeheader()
        i=0

        # Looping the data and loopoing the desired parsed data
        while True:

            # Wait until there is data waiting in the serial buffer
            if(serialPort.in_waiting > 0):

                # Read data out of the buffer until a carraige return / new line is found
                try:
                    line = serialPort.readline()
                    serialString = str(line, "ascii") #converting from bytes to string
                    serialSplit = serialString.split(' ')
                except:
                    print("Readline somehow messed up with the serial input")
                    break

                # Parsing
                serialParse = serialSplit[5] #taking element 5 which is 'addr2'
                serialParse = serialParse.replace("ADDR2=", "")
                serialParse = serialParse.replace(",", "")
                timeStamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

                # Print the contents of the serial data
                dw.writerow({"Timestamp": timeStamp, "ID": serialParse})
                currentTime = time.time();
                timePassed = currentTime - startTime;
                i += 1
                if timePassed > totalSeconds:
                    break;

    fileContent = pd.read_csv("data.csv")
    fileContent.to_excel("data.xlsx", index=None, header=True)
