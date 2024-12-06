# Arabic to Roman

def toRoman(n):
    numeral = ""

    while n >= 1000:
        n -= 1000
        numeral += "M"

    if n >= 900:
        n -= 900
        numeral += "CM"

    while n >= 500:
        n -= 500
        numeral += "D"

    if n >= 400:
        n -= 400
        numeral += "CD"

    while n >= 100:
        n -= 100
        numeral += "C"

    if n >= 90:
        n -= 90
        numeral += "XC"

    while n >= 50:
        n -= 50
        numeral += "L"

    if n >= 40:
        n -= 40
        numeral += "XL"

    while n >= 10:
        n -= 10
        numeral += "X"

    numeral += onetonine[n]

    return numeral



if __name__ == "__main__":
    for j in range(1,2345):
        ans = toRoman(j)
        if len(ans) <= len(str(j)):
            print((str(j)) + ": " + ans)