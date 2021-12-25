# Analyzing, Filtering, Parsing data from serial port

A simple program that is intended to work together with the microcontroler ESP32, WiFi Sniffer.
ESP32 network-interface that can do data in serial communication. 
Data is filtered and parsed data is stored onto the PC as a CSV and Excel file.
When it's finished sorting and storing data, the program calculates all MAC Addresses and gives a estimated number of how many unique devices are nearby.

Files:
* main.py = initialize whole program
* DataToCSV.py = Analyzing and parsing data from serial
* DataCalculation.py = Read, calculate and count how many devices nearby
* device_count.txt = Is the calculated data from 'DataCalculation.py'
* data100.csv = Is the sorted data that's saved into a CSV file
* data.csv = Is the sorted data that's saved into a CSV file
* data.xlxs = Is the sorted data that's saved into a Excel file.


In order for this program to work and to fully function, 
you'll are required to have the following: 

* IDE: Arduino(c++) and PyCharm(Python)
* Libraries: serial, csv, datetime, pandas
* Product: ESP32 (USB-connected to the PC)
* Excel (to check if the stored data is sorted and placed in correctly)

The Arduino coding part is taken from :
* https://github.com/ESP-EOS/ESP32-WiFi-Sniffer
* https://blog.podkalicki.com/esp32-wifi-sniffer/


