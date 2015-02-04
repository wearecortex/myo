import serial

ser = serial.Serial('/dev/ttyACM0', 9600)



rms_data = 66.875

ser.write(chr(254))
ser.write(chr(len(str(rms_data))))
ser.write(str(rms_data))

print rms_data
