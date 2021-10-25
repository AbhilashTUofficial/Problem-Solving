#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    hour=s[:2]
    mer=s[8:10]
    
    if(mer=='PM' and hour!="12"):hour=int(hour)+12            
    if(mer=='AM'and hour=='12'):hour='00'
    
    return f'{hour}:{s[3:8]}'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
