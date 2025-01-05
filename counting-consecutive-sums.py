# Experiments with consecutive sums

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

import time
def consec_id(n):
    m = 1

    index = 0

    value = 1
    viz = ""

    while n >= m:
        div = n/m
        if div == int(div):
            value *= primes[index]
            viz += str(index+1)
        else:
            viz += "-"
        n -= m
        m += 1
        index += 1

    return value,viz

if __name__ == "__main__":
    stopwatch = time.time()

    id_primes = []
    id_po2 = []


    for t in range(100):
        test = []
        for i in range(1000):
            x = consec_id(i)
            # if x == 2:                          # test for powers of 2 (works)
            #     id_po2.append(i)
            # if x == 6:                          # test for primes (works)
            #     id_primes.append(i)

            if x[0] == t:
                test.append(i)
                chime = x[1]
        if test:
            print(chime)
            print(test)

    print("\n/// done in " + str(time.time() - stopwatch) + " seconds ///")
