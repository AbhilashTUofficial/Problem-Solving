#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    
    n=0
    if any([False if i<=10 else True for i in B]): return 'NO'
    oddArr=[i for i in range(len(B))if B[i]%2!=0]
    if len(oddArr)==1: return 'NO'
    if len(oddArr)==0: return 0
    i,j=oddArr[0],oddArr[1]
    
    B[i]+=1
    B[i+1]+=1
    n+=2
    x= fairRations(B)
    if x=='NO': return 'NO'
    n+=int(x)  
    


    
    # while not all([True if i%2==0 else False for i in B]):
    
    
        
    return str(n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
