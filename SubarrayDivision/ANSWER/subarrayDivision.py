#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#
def segmentation(arr):
    # Function to get all segments from the array
    segments=[]
    for i in range(len(arr)):
        for j in range(len(arr)+1):
            if i<j:
                segments.append(arr[i:j])

    return segments


def birthday(s, d, m):
    n=0
    segments=segmentation(s)
    for x in segments:
        # check conditions
        if(len(x)==m and sum(x)==d):
            n+=1  
    return n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
