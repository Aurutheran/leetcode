#!/bin/python3

import math
import os
import random
import re
import sys

#Finish the code and make it better
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    contained = []
    unique = []
    duplicate = []
    sol = []
    for each in a:
        if each not in contained:
            contained.append(each)
            unique.append(each)
        else: 
            duplicate.append(each)
            unique.remove(each)
    return unique[0]
           
    
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
