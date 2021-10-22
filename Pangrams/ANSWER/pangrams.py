#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    string=[]
    [string.append(_) for _ in s.lower()]
    alpha=['a','b','c','d','e','f','g','h',
    'i','j','k','l','m','n','o','p','q','r',
    's','t','u','w','x','y','z']
    
    for x in alpha:
        if  x not in string:
            return 'not pangram'
    
    return 'pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
