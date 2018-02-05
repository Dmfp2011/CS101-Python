#####################################################
#####################################################
##  CS 101
##  Program 1
##  Dylan Pembrook
##  dmpfzf@mail.umkc.edu
##
##  Problem:Taking user input and
##  calculating drone flight time
##
##  Solution:
##      1. Get input from user regarding values of variables.
##          (int > 0)
##      2. Using input, calculate flight time of drone, in hours
##      3. Convert hours to minutes and seconds
##      4. Print results and enjoy
####################################################
####################################################

#User input to get specifications for calculations
#Converting str into int
milliamps_per_hour = int(input("What is the mAh?"))
motors = int(input("How many motors are there?"))
amps = int(input("How many amps per motor?"))

#Computing flight time in hours
amps_per_hour = milliamps_per_hour/1000
amp_usage = motors*amps
flight_per_hour = amps_per_hour/amp_usage

#Converting flight time from hours to minutes
flight_per_min = flight_per_hour*60

#Converting a decimal into minutes and seconds
minutes = int(flight_per_min//1)
seconds = int((((flight_per_min%1)*60)//1))

#Results
print()
print("Calculation Results")
print("Your drone will use", amp_usage ,"amps")
print("The flight time will be", flight_per_min, "minutes")
print("Which is",minutes,"minutes and",seconds, "seconds")

###########################################################
