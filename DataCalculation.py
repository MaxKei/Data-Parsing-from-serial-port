"""
DataCalculation.py : is made to read the sorted data, calculate and
count how many unique devices are nearby, which is later imported into a txt. file (device_count.txt)
"""
import csv
from datetime import datetime

def SaveDeviceCountToTXT():
    count = 0

    # output_dictionary = {'ID': 'Last Seen'}
    output_dictionary = {}

    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            ID = str(row["ID"])
            lastSeen_str = str(row["Timestamp"])
            lastSeen_dateTime = datetime.strptime(lastSeen_str, "%m/%d/%Y, %H:%M:%S")
            output_dictionary[ID] = lastSeen_dateTime

    sorted(output_dictionary)
    print()
    print('List of devices seen within', timeout_seconds, 'seconds:')
    print()
    for key in output_dictionary:
        print(key, 'was seen nearby')
        count = count + 1
    print()
    print(count, 'unique devices pinged esp32 in the last', timeout_seconds, 'seconds.')
    print()

    with open('device_count.txt', 'w') as f:
        f.write(count.__str__());
