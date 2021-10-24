#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    if(s==s[::-1]):return 0

    alpha=['a','b','c','d','e','f','g','h','i',
    'j','k','l','m','n','o','p','q','r','s',
    't','u','v','w','x','y','z']
    l=[]
    r=[]
    [l.append(_)for _ in s[:int(abs(len(s)/2))]]
    [r.append(_)for _ in s[-int(abs(len(s)/2)):]]
    
    steps=0
    
    for idx in range(len(l)):
        x=l[idx]
        y=r[::-1][idx]
        i=alpha.index(y)        
        j=alpha.index(x)
        
        steps+=abs(i-j)
    
    
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
