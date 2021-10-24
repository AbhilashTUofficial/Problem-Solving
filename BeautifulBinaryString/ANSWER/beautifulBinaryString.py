#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    
    s=[]
    count=0
    [s.append(_)for _ in b]
    for _ in range(len(b)):
        if "010" in b:
            i=b.index("010")
            s[i+2]="1"
            b=''.join(s)
            count+=1
        else:
            return count
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
