# 1.1.2025
# fun: storing telegram-style text (spaces, uppercase only) as a massive integer using prime factorization

import time

plist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def encode(slab):
    sutekh = 1

    raw = makelist(slab)

    index = 0

    for i in range(len(raw)):
        scale = plist[i] ** raw[i]
        sutekh *= scale


    print(sutekh)

def makelist(slab):
    data = []
    while slab:
        c = slab[0]
        a = alpha(c)
        if a:
            data.append(a)
        slab = slab[1:]

    for j in range(len(data)):
        data[j] = data[j] % 27

    return data

def alpha(c):
    if c == " ":
        return 27

    c = ord(c)

    if c < 65 or c > 122:
        return None
    if c > 90 and c < 97:
        return None

    if c > 96 and c < 123:
        c -= 32

    return c-64


def decode(scar):
    slab = ""
    for p in range(len(plist)):
        if scar % plist[p] == 0:
            n,power = collapse(scar,plist[p])
            slab += chr(power+64)
    print(slab)


def collapse(n,d):
    count = 0
    while n % d == 0:
        n = n//d
        count += 1
    return n,count


if __name__ == "__main__":
    stopwatch = time.time()

    #encode("Robyn (Skyrme) will find love, this year.")
    encode("RobynSkyrme")
    decode(212829922542622618414596524798553275737228835106637956506426909243757032415416781669198947230713336128506508713581324633156459529647797604275732143524740565378800025600)

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
