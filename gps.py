# code assumes a UDB GPS is plugged in. The system has placed it on COM3.  Your COM number may vary.
# Local Win10 also had U-center 22.07 installed

import serial

ser = serial.Serial('COM3', 9600, timeout=None)

gpsdata = ser.readline()
# next few lines just clean up the serial data

gpsdata = gpsdata.rstrip().lstrip()  # removes tail /r/n
gpsdata = gpsdata.decode("utf-8")
print(gpsdata)
gpsdatalist = gpsdata.split(",")
print(gpsdatalist)
# LATITUDE --- convert NMEA to decimal degree
# print("Latitude (degrees): ", gpsdatalist[3][0:2])
# print("Latitude (minutes): ", gpsdatalist[3][2:9])
deg = float(gpsdatalist[3][2:9])/60
# print("Latitude (degrees): ", deg)
lat = float(gpsdatalist[3][0:2]) + deg
print('Lat: ', str(lat)[0:8])

# LONGITUDE --- convert NMEA to decimal degree
# print("Longitude: ", float(gpsdatalist[5][0:3]))
# print("Longitude (minutes): ", gpsdatalist[5][3:10])
deg = float(gpsdatalist[5][3:10])/60
# print("Longitude (decimal): ", deg)
long = float(gpsdatalist[5][0:3]) + deg
long = long * -1
print('Long: ', str(long)[0:9])
