"""
Main.py - Autumn semester project
Copyright (c) 2021 by Max & Mansour.

This program is made for analyzing data coming from the serial port(USB)
It's especially made to work together with Arduino's service monitor.
The goal of this program is to have a live and automated dataflow that can be read & stored on the computer.
"""

# Importing serial = So that we can play with the USB data
# Importing CSV to be able to read and write CSV files
# Importing datetime for timestamps on the data
# Importing pandas for data analysis
import serial
import csv
from datetime import datetime
import pandas as pd


# Configuration for serial port
# COM4 is a specific USB-port
# Baudrate optimized for Arduino configuration
serialPort = serial.Serial(port = "COM4", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

serialString = ""                           # Used to hold data coming over UART
i = 0


# Settings for writing data

#f = open('data.csv', 'w', newline='', encoding='utf-8')


i = 0;


# While loop, including parsing and sorting the given data into a CSV.file
# Because we want to write and read sequences into CSV, we use the DictWriter & DictReader
# serialPort is the USB port, where the data is transferred and gathered into this program, and then decoded
# so that it's readable and sorted data which is put into a formatted excel file.
with open("data.csv", "w") as file:
    #fieldnames=['PACKET', 'CHAN', 'RSSI', 'ADDR1', 'ADDR2', 'ADDR3']
    fieldnames=['Timestamp', 'ID']
    dw = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
    dw.writeheader()

    while(i < 100):

        # Wait until there is data waiting in the serial buffer
        if(serialPort.in_waiting > 0):

            # Read data out of the buffer until a carraige return / new line is found
            serialString = str(serialPort.readline(), "ascii") #coverting from bytes to string
            serialSplit = serialString.split(' ')

            # Parsing
            lol = serialSplit[5]
            lol = lol.replace("ADDR2=", "")
            lol = lol.replace(",", "")
            time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

            # Print the contents of the serial data
            dw.writerow({"Timestamp": time, "ID": lol})

            i+=1

fileContent = pd.read_csv("data.csv")
fileContent.to_excel("data.xlsx", index=None, header=True)