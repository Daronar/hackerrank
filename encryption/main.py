#!/bin/python
# code for https://www.hackerrank.com/challenges/encryption/problem

import math
import os
import random
import re
import sys


def choose_row_and_col_nums(length):
    row_num = int(length ** 0.5)
    col_num = row_num
    if row_num * col_num >= length:
        return row_num, col_num
    col_num += 1
    if row_num * col_num >= length:
        return row_num, col_num
    row_num += 1
    if row_num * col_num >= length:
        return row_num, col_num


# Complete the encryption function below.
def encryption(s):
    s = filter(lambda x: x != ' ' and x != '\n', s)
    rows, cols = choose_row_and_col_nums(len(s))
    length = len(s)
    assert rows * cols >= length
    enmas = []
    for i in xrange(rows):
        start = i * cols
        end = i * cols + cols if i * cols + cols <= length else length
        enmas.append(s[start: end])
    answer = []
    for j in xrange(cols):
        new_word = []
        for i in xrange(rows):
            if j < len(enmas[i]):
                new_word.append(enmas[i][j])
        answer.append(''.join(new_word))
    msg = ' '.join(answer)
    return msg


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
