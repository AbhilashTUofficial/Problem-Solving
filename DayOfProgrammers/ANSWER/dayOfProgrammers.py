#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):

    cal=[31,28,31,30,31,30,31,31]
    

    def leapDay():
        if year<=1917:
            if year%4==0:
                return -1            
        else :
            if (year%400==0 or year%4==0 and year%100!=0):
                return -1
            
        return 0
        
    
    
    if(year==1918):
        return str(13+leapDay()+13)+".09."+str(year)
                
    return str(13+leapDay())+".09."+str(year)
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
