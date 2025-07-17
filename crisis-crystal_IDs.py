def get_alphanum(char):

    asc = ord(char)

    if asc < 65:
        return 1

    if asc > 90:
        asc -= 32

    if asc > 90:
        return 1

    asc -= 64

    n = asc

    return n

if __name__ == "__main__":

    mult = 1

    for char in "AlexPaigeNell":
        c = get_alphanum(char)
        mult *= c

    print(mult)