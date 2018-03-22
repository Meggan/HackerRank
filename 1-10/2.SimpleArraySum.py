#!/bin/python

from __future__ import print_function

import os
#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    count = 0;
    while count < len(ar):
        res += ar[count]
        return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

