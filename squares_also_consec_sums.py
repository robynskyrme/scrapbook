def sq_also_consec(n):
    sq = n**2
    sum = n
    m = n

    while sum < sq:
        m += 1
        sum += m

    if sum == sq:
        print (n)
    else:
        return False

for i in range(10000):
    sq_also_consec(i)