#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
#You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

hours=int(input("Enter number of Hours:"))
Rate=float(input("Enter rate per hour:"))
Gross_Pay=float(hours*Rate)
print("Pay:",Gross_Pay)
