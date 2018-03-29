#!/bin/python3

import os
import sys

def aVeryBigSum(n, ar):
    bigsum = 0
    index = 0
    for n in ar:
        bigsum += ar[index]
        index += 1

    return bigsum

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()
