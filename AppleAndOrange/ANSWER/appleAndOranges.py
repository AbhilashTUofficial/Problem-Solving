#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    # print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
    # print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))
    

    # Calculate the distance the fruit fall.
    appleDist=[]
    orangeDist=[]
    for apple in apples:
        appleDist.append(a+apple)
    for orange in oranges:
        orangeDist.append(b+orange)
        
    # Check, is the fruit fall to the house?
    appleCount=0
    orangeCount=0
    for apple in appleDist:
        if(apple >=s and apple <=t):
            appleCount+=1
    for orange in orangeDist:
        if(orange <=t and orange >=s):
            orangeCount+=1
    
    print(appleCount)
    print(orangeCount)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
