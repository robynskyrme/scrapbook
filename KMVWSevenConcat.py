# 7.4.2024
# from Karl M V Waugh:
#
# Here's a fun puzzle you might enjoy.
#
# Take an integer N and concatenate it with itself 6 times. eg.
# 666,666 or 121,212,121,212
#
# when is this number divisible by 7?
#
# I have a proof but even beyond that I wonder if you can find the situations it is / isn't.

import math

def concat(a,b):
    n = 0
    a = a * 10 ** (math.floor(math.log(b,10)+1))
    n = a + b
    return n


def divides(n,d):
    if n % d == 0:
        return True
    else:
        return False

def mults(lower,upper,d):
    for i in range(upper,lower):
        c = i
        for j in range(5):
            c = concat(i, c)
        if not divides(c,d):
            print(str(i) + ": " + str(c))




if __name__ == "__main__":
    mults(99999,111111,7)