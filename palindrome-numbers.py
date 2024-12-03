# Messing around with palindromes, finding shortcuts etc.

def reverse(n):
    s = str(n)
    output = ""
    while s:
        output = s[0] + output
        s = s[1:]
    return int(output)


if __name__ == "__main__":
    for i in range(1235):
#        print(i)
        print(str(reverse(i)))