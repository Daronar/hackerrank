#!/bin/python

import math
import os
import random
import re
import sys


def _get_count_of_digits(p):
    count = 0
    while p > 0:
        count += 1
        p /= 10
    return count


def _split_number_by_len(p, d):
    l = r = 0
    counter = 0
    while counter < d:
        r += (10 ** counter) * (p % 10)
        p /= 10
        counter += 1
    counter = 0
    while p > 0:
        l += (10 ** counter) * (p % 10)
        p /= 10
        counter += 1
    return l, r


def _is_kaprekar_number(p):
    d = _get_count_of_digits(p)
    l, r = _split_number_by_len(p**2, d)
    return l+r == p

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    x = p
    kap = []
    while x <= q:
        if _is_kaprekar_number(x):
            kap.append(str(x))
        x += 1
    if len(kap) == 0:
        print 'INVALID RANGE'
    else:
        print ' '.join(kap)

if __name__ == '__main__':
    p = int(raw_input())

    q = int(raw_input())

    kaprekarNumbers(p, q)

