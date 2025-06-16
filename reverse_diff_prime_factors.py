import math

def reverse(n) -> int:

    ans = 0

    while n:

        ans *= 10
        ans += n % 10
        n = n//10

    return ans


def prime_factors(n):
    if n == 0:
        return [],0
    factors = []

    candidate = 2

    while n != 1:
        if n % candidate == 0:
            n = n/candidate
            factors.append(candidate)
            candidate = 1
        candidate += 1

    return factors,sum(factors)



if __name__ == "__main__":

    sum_list = []

    for i in range(10000,20000):
        rev = reverse(i)
        p = prime_factors((int(math.fabs(i-rev))))

        sum_list.append(p[1])

        # print(i,"-",rev,p)

    for sum in sum_list:
        print(sum)