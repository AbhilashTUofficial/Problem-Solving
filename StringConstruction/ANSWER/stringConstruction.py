#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):

    choosenLetter=[]
        
    # for x in [_ for _ in s][::-1]:
    #     if(x not in choosenLetter):
    #         choosenLetter.append(x)
            
    [choosenLetter.append(x)for x in [_ for _ in s][::-1]if(x not in choosenLetter)]
    
    return len(choosenLetter)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
