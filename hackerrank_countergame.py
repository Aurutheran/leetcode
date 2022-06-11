#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def get_mask(n):
    return 1 << math.floor(math.log(n,2))

def counter_game(n):
    winner = 0
    while n != 1:
        mask = get_mask(n)
        if mask == n:
            n = n/2
        else:
            n -= mask
            
        winner ^= 1
    
    
    if winner == 1:
        return "Louise"
    elif winner == 0:
        return "Richard"
        
        

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counter_game(n)

        fptr.write(result + '\n')

    fptr.close()
