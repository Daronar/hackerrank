#!/bin/python

import math
import os
import random
import re
import sys

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = raw_input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in xrange(p):
        astronaut.append(map(int, raw_input().rstrip().split()))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()