import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    n=len(grades)
    finalGrades=[]
    for i in grades:
        if( i <38 ):
            finalGrades.append(i)
        else:
            k=5*math.ceil(i/5)
            if(-3<i-k<3):
                finalGrades.append(k)
            else:
                finalGrades.append(i)
    
    return finalGrades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
