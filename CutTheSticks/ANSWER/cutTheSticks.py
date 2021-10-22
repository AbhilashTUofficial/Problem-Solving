#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def flattenArray(arr):
    arr2=[]
    for i in arr:
        if(isinstance(i,int)):
            arr2.append(i)
        else:
            arr2.extend(flattenArray(i))
    return arr2

def cutTheSticks(arr):
    n=len(arr)
    if(n<=0):return []
    if(n==1):return [1]
    s=min(arr)
    for i in range(n):
        arr[i]-=s
    arr=[i for i in arr if i!=0]
        
    return flattenArray([n,cutTheSticks(arr)])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
