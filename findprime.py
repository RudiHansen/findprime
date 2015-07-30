#!/usr/bin/python
import os.path
import sys
import time
import math

fileNameTxt = 'findprime.txt'
fileNameSta = 'findprime.sta'
CONST_NUMFIND = 1000

# Method to test if a number is a prime number
def is_prime(n):
    if n % 2 == 0 and n > 2: 
	return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
	if n % i == 0:
	    return False
    return True

# Append Prime number to file
def writeLog(n):
    outputfile = open(fileNameTxt, 'a')
    outputfile.write(str(n) + "\n")
    outputfile.close()
    
# Save Prime number to status file
def writeStatus(n):
    outputfile = open(fileNameSta, 'w')
    outputfile.write(str(n) + "\n")
    outputfile.close()
    
# Read last Prime number from status file
def readStatus():
    if os.path.isfile(fileNameSta):
        inputfile = open(fileNameSta, 'r')
	indata = inputfile.read()
	lastPrimeNum = long(indata)
        inputfile.close()
        return lastPrimeNum
    else:
	return 1
        

# Python program to ask the user for a range and display all the prime numbers in that interval

# take input from the user
num = readStatus()
startTime = time.time()

try:
    while True:
        # prime numbers are greater than 1
	if is_prime(num):
	    lastprime = num
	    writeLog(num)
	    writeStatus(num)
	num += 1
	# Output progress
	if num % CONST_NUMFIND == 0:
	    elapsedTime = time.time() - startTime
	    txt = 'Last prime %i, checked %i numbers in %0.3f seconds' % (lastprime,CONST_NUMFIND,elapsedTime)
	    sys.stdout.write("\r" + txt)
	    sys.stdout.flush()
	    startTime = time.time()
	
except KeyboardInterrupt:
    pass
    
