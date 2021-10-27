#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    
    # n//c return how many c in n 
    # while n/c simple return n/c
    bars = n//c
    w = bars
    while w>=m:
        a,b = divmod(w,m)
        bars+=a
        w = a+b
    return bars
        
    # Problem with floating point values
    # w=n/c
    # bars=w
    # bw=0
    # while w>=m:
    #     bw=bars/m
    #     w+=bw
    #     bw+=bars%m
    #     bars=bw
        
    # return math.floor(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
