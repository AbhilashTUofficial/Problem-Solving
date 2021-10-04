#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n,N):
    
    if n==1:return 2,2
    l,c=viralAdvertising(n-1,N)
    l=math.floor(l*3/2)
    c=c+l
    if n==N:return c
    return l,c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n,N=n)

    fptr.write(str(result) + '\n')

    fptr.close()
