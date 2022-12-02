import tkinter as tk
from tkinter import filedialog
import csv

root = tk.Tk()
root.withdraw()
print("Click on the file with all the students who are registered for the trip:")
file_registered = filedialog.askopenfile()
print(file_registered)
print("Click on the file with all the students on the waitlist:")
file_waitlist = filedialog.askopenfile()
print(file_waitlist)
output_name = input("What would you like the file to be called? If you would like to exit the program, type 'quit'\n")
if output_name == 'quit':
    quit()
output_name += '.csv'

output = open(output_name, "w")

first_name = []
last_name = []
uid = []
email = []
emergency_contact = []
registration_date = []

reg = csv.reader(file_registered, delimiter=',')
length = 0   
for r in reg:
    if length != 0:
        first_name.append(r[18])
        last_name.append(r[19])
        uid.append(r[10])
        email.append(r[11])
        emergency_contact.append(r[29])
        registration_date.append(r[26])
    length += 1

output.write("Name, UID / Member #, Email Address, Emergency Contact, Registration Date\n")

for i in range(0, length-1):
    output.write(str(first_name[i]) + ' ' + str(last_name[i]) + ',"' + str(uid[i]) +  '",' + str(email[i]) + ',' + str(emergency_contact[i]) + ',' + str(registration_date[i]) + '\n')

w_name = []
w_uid = []
w_email = []
w_emergency_contact = []

wait = csv.reader(file_waitlist, delimiter=',')
length = 0
for r in wait:
    if length != 0:
        w_name.append(r[2])
        w_uid.append(r[4])
        w_email.append(r[6])
        w_emergency_contact.append(r[5]) 
    length += 1

output.write("\nWaitlist, , , , \n")

for i in range(0, length-1):
    output.write(str(w_name[i]) + ',' + str(w_uid[i]) +  ',' + str(w_email[i]) + ',' + str(w_emergency_contact[i]) + ',\n')

output.close()

print(output)