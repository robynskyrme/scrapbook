# tracking the last digits of [initially] 2x + 1 modulo n

import math

def show_patterns(n):

    digits = []

    for i in range(n):
        digits.append((i * 3 + 1) % n)                  # trying 3x + 1


    cycles = []
    cycle_sets = []

    for j in range(n):
        cycle = []
        digit = j
        while digit not in cycle:
            cycle.append(digit)
            digit = digits[digit]

        cycleset = set(cycle)
        if cycleset not in cycle_sets:
            cycles.append(cycle)
            cycle_sets.append(cycleset)

    return cycles



def prime(n):
                                # Special cases:
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True

    max = (int(math.ceil(math.sqrt(abs(n)))))

    sieve = [0]

    for s in range(max):
        sieve.append(1)

    d = 2
                                # Count up to sqrt(n)
    while d <= max:
                                # Only check a new divisor if it has not already been eliminated
        if sieve[d] == 1:
            if n % d == 0:
                return False
                                # If a number d does not divide n, then eliminate all multiples of d from the search
        for j in range(d,len(sieve),d):
            sieve[j] = 0
        d += 1

    return True



if __name__ == "__main__":

    for p in range(20):
        #cycle_counts = []

        cycles = show_patterns(p)
        print("\n",p)
        for c in cycles:
            print(c)


