# Program listens to the serial monitor and
# writes each value to a CSV file
import serial
import csv

# --------------------
# NEED TO SET CONFIGS BELOW:
# --------------------
baudRate = 9600
comPort = 'COM3'
csvFileName = '\Temp\data.csv'
# -------------------- 

# Set the baud rate and COM port
ser = serial.Serial()
ser.baudrate = baudRate
ser.port = comPort

# Open connect to the serial port
ser.open()  

# Open a CSV file for writing 
with open(csvFileName, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)   
    line = ' ';
    while (True):
        line = ser.readline()
        print(line)
        csvwriter.writerow( str(line) )
    
ser.close()  # close connection to serial port
