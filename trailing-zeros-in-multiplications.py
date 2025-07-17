import random

def count_right_zeroes(n):

    count = 0

    while n % 10 == 0:
        count += 1
        n = n/10

    return count



def get_average_zeroes(digits,howmany,rolls):
    zeroes = []
    ceiling = (10 ** digits) - 1

    for i in range(rolls):
        values = []

        for j in range(howmany):
            values.append(random.randint(1,ceiling))

        n = 1
        for v in values:
            n = n*v

        #print(values,n)
        zeroes.append(count_right_zeroes(n))

    average = sum(zeroes) / len(zeroes)
    print(average)


if __name__ == "__main__":
    get_average_zeroes(3,40,10000)