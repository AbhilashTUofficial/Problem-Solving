#!/bin/python3

import math
import os
import random
import re
import sys
import string
#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    res={}
    for letter in string.ascii_lowercase:
        for height in h:
            res[letter] = height
            h.remove(height)
            break
    return max(res[w]for w in word)*len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
