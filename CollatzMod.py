# Collatz sequence without 'if' statement

def collatz(n):
    n = (n + ((n % 2) * (2 * n + 1 ))) // (2 - n % 2)
    return n

def collatz_seq(n):
    seq = [n]

    while n != 1:
        n = collatz(n)
        seq.append(n)

    return seq


if __name__ == "__main__":
    print(collatz_seq(73))