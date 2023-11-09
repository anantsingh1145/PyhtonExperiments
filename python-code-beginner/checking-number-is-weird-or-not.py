#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input(print("enter the number :- ")).strip())
    if n%2 == 1:
        print("Weird")
    elif n in range (2, 5):
        n%2 == 0
        print("Not Weird")
    elif n in range(6, 20):
        n%2 == 0
        print("Weird")
    elif n>=20:
        n%2 == 0
        print("Not Weird")