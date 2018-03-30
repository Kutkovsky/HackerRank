#!/bin/python3

import os
import sys

def diagonalDifference(a):
    diff = 0
    a_len = len(a)
    for idx in range(a_len):
        diff += a[idx][idx]
        diff -= a[idx][a_len-idx-1]
 
    return abs(diff)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
