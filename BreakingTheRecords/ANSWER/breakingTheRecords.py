#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    n=len(scores)
    high=scores[0]
    low=scores[0]
    bRec=0
    wRec=0
    
    for i in range(n):
        if(high<scores[i]):
            high=scores[i]
            bRec+=1
        if(low>scores[i]):
            low=scores[i]
            wRec+=1
            
    
        
    return [bRec,wRec]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
