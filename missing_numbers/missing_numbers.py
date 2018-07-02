#!/bin/python

import math
import os
import random
import re
import sys


# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    arr = arr.sort()
    brr = brr.sort()
    missing = []
    i, j = 0, 0
    len_arr = len(arr)
    len_brr = len(brr)
    while i < len_arr:
        if arr[i] == brr[j]:
            i += 1
            j += 1
        else:
            missing.append(brr[j])
            j += 1


    return []

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    m = int(raw_input())

    brr = map(int, raw_input().rstrip().split())

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
