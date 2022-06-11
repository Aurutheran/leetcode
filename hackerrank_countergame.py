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


def counter_game(n):
    
    winner = ["Louise","Richard"]  
    
    count = 0
    vals = n
    
    if (vals==1):
        return winner[0]
    
    
    while(vals != 1):
        moduli = vals - 2**(math.log(vals)//math.log(2))
    
        if (moduli != 0):
            vals = moduli
        else:
            vals = vals/2
        
        if vals != 1:
            count += 1
        
    return winner[count%2]
        

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counter_game(n)

        fptr.write(result + '\n')

    fptr.close()
