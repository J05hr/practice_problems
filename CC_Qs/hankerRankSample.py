#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for idx in range(1, n):
        if idx % 3 == 0 and idx % 5 == 0:
            print("FizzBuzz")
        elif idx % 3 == 0 and idx % 5 != 0:
            print("Fizz")
        elif idx % 3 != 0 and idx % 5 == 0:
            print("Buzz")
        else:
            print(idx)