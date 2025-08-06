import math

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



def reverse(n):
    s = str(n)
    output = ""
    while s:
        output = s[0] + output
        s = s[1:]
    return int(output)



def gen_prime_list(ceil):
    primes = []
    c = 2
    while c <= ceil:
        if prime(c):
            primes.append(c)
        c += 1

    return(primes)


if __name__ == "__main__":
    primes = gen_prime_list(100000)                       # list the primes
    #print("Primes:\n",primes,"\n")
    prime_reverses = []
    for p in primes:
        if reverse(p) in primes:
            prime_reverses.append(p)

    #print("Primes whose reverse is also a prime:\n",prime_reverses,"\n")

    print("The above list, whose index, in the list, reversed, is the index of the reversed prime:\n")

    for p in enumerate(primes):
        index = p[0]+1
        prime = p[1]
        if reverse(index)-1 < len(primes):
            if primes[reverse(index)-1] == reverse(prime):
                print(index,reverse(index),prime,primes[reverse(index)-1])