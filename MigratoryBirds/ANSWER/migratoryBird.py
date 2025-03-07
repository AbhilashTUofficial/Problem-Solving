#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    
    arr=sorted(arr)
    arrY,arrX=[],[]
    [arrX.append(_) for _ in arr if _ not in arrX]
    [arrY.append(arr.count(_)) for _ in arrX]
        
    
    return arrX[arrY.index(max(arrY))]

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
