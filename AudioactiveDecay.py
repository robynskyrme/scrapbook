# see The Weird and Wonderful Chemistry of Audioactive Decay by J.H. Conway (Eureka magazine, 1986)

def derive(n: int) -> int:
    n = str(n)

    char = n[0]
    count = 0

    derived = ""

    for caret in n:
        if caret == char:
            count += 1
        else:
            derived = derived + str(count) + str(char)
            count = 1
            char = caret

    derived = derived + str(count) + str(char)

    return(derived)

def decay(start,days):
    for d in range(days):
        print(start)
        start = derive(start)
    print(start)


if __name__ == "__main__":
    decay(1,19)