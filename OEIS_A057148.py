def A057148(n):
    if n == 1: return 0
    a = 1<<n.bit_length()-2
    s = bin(a|(n&a-1))[2:]
    return int(s+(s[::-1] if a&n else s[-2::-1]))


for j in range(1,45):
    print (A057148(j))