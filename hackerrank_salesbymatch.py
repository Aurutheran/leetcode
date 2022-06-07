#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    
    #Array Containing Socks we added (Will check them for duplicates to find pairs)
    sock_pairs = []
    count = 0
    
    #If the socks are in the array, we increment and remove that sock.
    #If the sock isn't in the array, we add it to the array to further check it in the 
    #Upcoming iterations of the for-loop
    
    for socks in ar:
        if socks not in sock_pairs:
            sock_pairs.append(socks)
        elif socks in sock_pairs:
            sock_pairs.remove(socks)
            count += 1
            
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
