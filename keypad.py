# (not serious)
# Code to calculate differences between numbers as entered in a keypad which has been rotated or reflected

import time


def reflect_y(n):
    new = [0,3,2,1,6,5,4,9,8,7]
    s = str(n)
    output = ""
    for i in s:
        output += str(new[int(i)])

    output = int(output)
    return output

def reflect_x(n):
    new = [0,7,8,9,4,5,6,1,2,3]
    s = str(n)
    output = ""
    for i in s:
        output += str(new[int(i)])

    output = int(output)
    return output

def reflect_diagback(n):
    new = [0,1,4,7,2,5,8,3,6,9]
    s = str(n)
    output = ""
    for i in s:
        output += str(new[int(i)])

    output = int(output)
    return output

def reflect_diagfwd(n):
    new = [0,9,6,3,8,5,2,7,4,1]
    s = str(n)
    output = ""
    for i in s:
        output += str(new[int(i)])

    output = int(output)
    return output


if __name__ == "__main__":
    stopwatch = time.time()

    for i in range (10000):
        print(i - reflect_diagfwd(i))


    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
