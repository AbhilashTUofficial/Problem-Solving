#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    arr=sorted(arr)
    print(sum(arr[:-1]),sum(arr[1:]))
    

# Noob code
# 
# def calcSum(arr):
#     sum=0
#     for i in arr:
#         sum+=i
        
#     return sum
# def miniMaxSum(arr):      
#     arr=sorted(arr)
#     n=len(arr)
#     minArr=arr[:n-1]
#     maxArr=arr[-(n-1):]
#     minVal= calcSum(minArr)
#     maxVal= calcSum(maxArr)
    
#     print(minVal,maxVal)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
