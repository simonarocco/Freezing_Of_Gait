import serial
import csv
import matplotlib

def name_file():
    print("Enter file name: ")
    file_name = input() + ".csv"
    return file_name

def process_string(raw_string):
    clean_string = raw_string[9:-5]
    return float(clean_string)

acz = []
acy = []
acx = []
ser = serial.Serial("/dev/cu.usbmodem1451", 9600)
ser.reset_input_buffer()
count = 0
while count <= 1000:
    raw_string = str(ser.readline())
    print(raw_string)
    if "Acc z" in raw_string:
        acz.append(process_string(raw_string))
    elif "Acc y" in raw_string:
        acy.append(process_string(raw_string))
    elif "Acc x" in raw_string:
        acx.append(process_string(raw_string))
    #print(raw_string)
    # clean_string = process_string(raw_string)
    count += 1

print(len(acz))
print(len(acx))
print(len(acy))

with open(name_file(), 'w') as csvfile:
    filewriter = csv.writer(csvfile)
    count = 0
    values = zip(acx, acy, acz)
    filewriter.writerow(("AcX", "AcY", "AcZ"))
    filewriter.writerows(values)
csvfile.close()