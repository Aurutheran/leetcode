#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    max = -sys.maxsize-1
    min = sys.maxsize
    sum = 0
    for each in arr:
        sum += each
        if each>max:
            max = each
        if each<min:
            min = each
    print(sum-max,sum-min)
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
