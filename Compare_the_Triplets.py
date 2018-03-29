#!/bin/python3

import os
import sys

def solve(a0, a1, a2, b0, b1, b2):
    A_score = 0
    B_score = 0
    for index in range (0, 3):
        if int(a0A1A2[index]) > int(b0B1B2[index]):
            A_score += 1
        elif int(a0A1A2[index]) < int(b0B1B2[index]):
            B_score += 1
        else:
            pass
    
    return A_score, B_score

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
