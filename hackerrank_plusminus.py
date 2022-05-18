#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos=neg=zer=0
    total = len(arr)
    for i in arr:
        if i>0:
            pos += 1
        elif i==0:
            zer += 1
        else:
            neg += 1
    print(float(round((pos/total),6)))
    print(float(round((neg/total),6))) 
    print(float(round((zer/total),6)))  
       
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)