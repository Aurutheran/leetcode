#!/bin/python3

import math
import os
import random
import re
import sys

#INCOMPLETE
#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
def xor(a,b):
    return(a and not b) or (not a and b)
def sumXor(n):
    # Write your code here
    count = 0
    if n==0:
        return 1
    for x in range(n):
        first = x ^ n
        second = x + n
        if (first == second):
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
