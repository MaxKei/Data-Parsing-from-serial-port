"""
Main files: DataToCSV.py , main.py , DataCalculation.py
Autumn semester project - Copyright (c) 2021 by Max & Mansour.

This program is made for analyzing data coming from the serial port(USB)
It's especially made to work together with Arduino's service monitor and the WiFi-Sniffer code from https://github.com/ESP-EOS/ESP32-WiFi-Sniffer.
The goal of this program is to have a live and automated dataflow that can be read & stored on the computer.
"""
# Run ' main.py ' to initialize the whole program.

import DataToCSV
import DataCalculation
import time

while True:
    DataToCSV.SaveDatatoCSV()
    print("CSV Loaded...")
    DataCalculation.SaveDeviceCountToTXT()
    print("TXT Loaded...")
    time.sleep(5)
