# bit of fun
# return whether a string contains letters sufficient to make this:
# REDORANGEYELLOWGREENBLUEINDIGOVIOLET
# once, or even twice

import random

def genstring(k):
    output = ""
    for i in range(k):
        output += chr(random.randint(1,26)+64)

    return output




if __name__ == "__main__":
    for i in range(50):
        j = random.randint(10,250)
        print(genstring(j))