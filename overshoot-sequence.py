


def reverse(n) -> int:
    ans = 0
    while n:
        ans *= 10
        ans += n % 10
        n = n//10
    return ans

def overshoot(n) -> int:
    m = reverse(n)

    data = []

    if m % n == 0:
        return 0

    count = n

    while count <= m:
        data.append(count)
        count += n

    data.append(count)
    data.append(count-m)

    return data[-1]

if __name__ == "__main__":
    for i in range(2,12345):
        print(overshoot(i))