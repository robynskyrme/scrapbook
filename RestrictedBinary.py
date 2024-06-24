# 25.3.2024
# Count in binary with only certain numbers of zeros or ones available, showing which integers can and can't be made

def restrictedBinary(o,z):

    limit = (2 ** (o+z+1)) - (2 ** z+1)

    sequence = []

    limit += 1

    for count in range(limit):
        if binarypossible(count,o,z):
            sequence.append(count)

    return sequence


def binarypossible(n,o,z):
    binstr = bin(n)[2:]
    # print(binstr)

    if len(binstr) > o+z:
        return False

    if binstr.count("0") > z:
        return False

    if binstr.count("1") > o:
        return False

    #print(binstr + " = " + str(n))

    print(str(n))

    return True







if __name__ == "__main__":
    seq = (restrictedBinary(11,4))
    #print (seq)