#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    
    arrA1,arrA2,arrX1,arrX2=[],[],[],[]
    
    [arrA1.append(ord(_))for _ in [_ for _ in s]]    
    arrA2=arrA1[::-1]
    
    [arrX1.append(abs(arrA1[i]-arrA1[i+1]))for i in range(len(arrA1)-1)]
    [arrX2.append(abs(arrA2[i]-arrA2[i+1]))for i in range(len(arrA2)-1)]
    
    if(arrX1==arrX2):
        return "Funny"
        
    
    return 'Not Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
