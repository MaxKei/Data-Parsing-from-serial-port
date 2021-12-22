# Analyzing-Data-from-USB-port

A simple program that is intended to work together Arduino's data from the serial monitor.
It's programmed so that the data from the Arduino is stored on the PC in a CSV and Excel file.


Files:
* main.py = the code
* data.csv = is the sorted data that's saved into a CSV file
* data.xlxs = is the sorted data that's saved into a Excel file.


In order for this program to work and to fully functionate, 
you'll be needing the following: 

* IDE: Arduino and Python
* Libraries: serial, csv, datetime, pandas
* Product: ESP32 (USB-connected to the PC)
* Excel (to check if the stored data is sorted and placed in correctly)

The Arduino coding part is taken from :
* https://github.com/ESP-EOS/ESP32-WiFi-Sniffer
* https://blog.podkalicki.com/esp32-wifi-sniffer/

