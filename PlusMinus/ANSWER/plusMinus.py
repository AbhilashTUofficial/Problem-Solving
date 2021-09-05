#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    x=len(arr)
    n=p=z=0
    for i in arr:
        if(i==0):
            z+=1
        elif(i<0):
            n+=1
        elif(i>0):
            p+=1
    print(p/x)
    print(n/x)
    print(z/x)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
