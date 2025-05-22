def antihydra(n,stop):
    oddcount = 0

    odometer = 0

    while oddcount >= 0 and odometer < stop:
        odometer += 1
        if n % 2 == 0:
            print("       ",n)
            oddcount += 2
        else:
            print(n)
            oddcount -= 1
        n = n + n // 2







if __name__ == "__main__":
    antihydra(8,50)