# 19.5.2024
# Convert numbers to different bases

                            # function converts decimal number n, returns it in base b (as a string)
def rebase(n,b):
    if n < b:
        return n

    power = 0
    ans = []

    while b ** power <= n:
        power += 1

    power -= 1

    while power > -1:
        rem = n % b ** power
        digit = (n - rem) // b ** power
        ans.append(digit)
        n = rem
        power -= 1

    string = ""
    for d in ans:
        string += str(d)

    return string



if __name__ == "__main__":
    print(rebase(32752,2))