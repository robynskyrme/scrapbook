# code suggested by MWH for a proofreading task involving adding "A.D." to all dates in a piece of text


import time



text = ""
extra = "A.D."

def isnum(c):
    if ord(c) < 48 or ord(c) > 57:
        return False
    return True

def copy_add(text):
    new = ""

    pointer = 0
    numcount = 0

    while pointer < len(text):
        new += text[pointer]
        if isnum(text[pointer]):
            numcount += 1
        else:
            numcount = 0


        if numcount > 3:
            new += extra

        pointer += 1

    return new



if __name__ == "__main__":
    stopwatch = time.time()

    text = "fox1949"

    text = copy_add(text)

    print(text)


    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
