#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    val = str(n)*k
    
    def recurs(n):
        total = 0
        for each in str(n):
            total += int(each)
        
        total = str(total)
        if len(total) == 1:
            return int(total)
        else:
            return recurs(total)
        
    inputs = str(n)*k
    
    return recurs(inputs)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
