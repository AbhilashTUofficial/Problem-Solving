#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    
    comb=[]
    [comb.append(i+j) for i in keyboards for j in drives if (i+j)<=b]
    
    # for i in keyboards:
    #     for j in drives:
    #         if (i+j <=b):
    #             comb.append(i+j)
    
    return max(comb) if comb!=[] else -1

    # Stupid code
    
    # kb=sorted(keyboards)
    # pd=sorted(drives)
    
    # balance=[]
    
    # for i in kb:
    #     bal=b-i
    #     if(bal>0):
    #         for j in pd:
    #             comb.append([i,j])
    #             balance.append(bal-j if bal-j>0 else -1)
    
    # return sum(comb[balance.index(sorted(balance)[1])]) if len(balance)>1 else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
