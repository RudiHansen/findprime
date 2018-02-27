#!/usr/bin/python
import os
import os.path
import sys
import time
import math
from time import sleep
from curses import wrapper

fileNameTxt = 'findprime.txt'
fileNameSta = 'findprime.sta'
CONST_NUMFIND = 5000

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

def main(stdscr):
    startPrimeNum = readStatus()
    startTimeMain = time.time()
    startTime = time.time()
    

    # Clear screen
    stdscr.clear()
    stdscr.addstr(1, 5 , 'Start from prime number  : {0}'.format(startPrimeNum))
    stdscr.addstr(1, 50, 'Start time : {0}'.format(time.strftime('%H:%M:%S',time.localtime(startTimeMain))))
    stdscr.refresh()
    num = startPrimeNum
    
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
                runTime = time.time() - startTimeMain
                totalPrime = num-startPrimeNum
                stdscr.addstr(2, 5 , 'Total prime number found : {0}'.format(totalPrime))
                stdscr.addstr(2, 50, 'Run time   : {0}'.format(time.strftime('%H:%M:%S',time.gmtime(runTime))))
                
                elapsedTime = time.time() - startTime
                stdscr.addstr(4, 5, 'Last prime : {0}'.format(lastprime))
                stdscr.addstr(5, 5, 'Checked {0} numbers in {1:.2f} seconds'.format(CONST_NUMFIND,elapsedTime))
                stdscr.refresh()
                startTime = time.time()
	
            sleep(0.001)
    
    except KeyboardInterrupt:
        print '\nDone'
        pass

wrapper(main)        
