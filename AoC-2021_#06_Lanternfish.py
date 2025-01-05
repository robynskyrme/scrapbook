# 5.1.2025

# AoC 2021 Day 6: Lanternfish

import time

def tabulate(input):
    list = [0,0,0,0,0,0,0,0,0]            # value of nth index = how many fish have 'n' days left

    for i in range(9):
        list[i] = input.count(i)

    return list


def gen_days(fish,days):

    if days == 0:                       # escape recursion
        return fish

    p = fish.pop(0)                     # this value is the number of fish on 'day zero'

    fish.append(p)                      # for each of those fish, a new fish on 'day eight' is added
    fish[6] += p                        # and each of those fish is reset to day 7
    print(fish)

    days -= 1                           # behave recursively
    fish = gen_days(fish,days)

    return fish



if __name__ == "__main__":
    stopwatch = time.time()

    aoc_input = [3,5,4,1,2,1,5,5,1,1,1,1,4,1,4,5,4,5,1,3,1,1,1,4,1,1,3,1,1,5,3,1,1,3,1,3,1,1,1,4,1,2,5,3,1,4,2,3,1,1,2,1,1,1,4,1,1,1,1,2,1,1,1,3,1,1,4,1,4,1,5,1,4,2,1,1,5,4,4,4,1,4,1,1,1,1,3,1,5,1,4,5,3,1,4,1,5,2,2,5,1,3,2,2,5,4,2,3,4,1,2,1,1,2,1,1,5,4,1,1,1,1,3,1,5,4,1,5,1,1,4,3,4,3,1,5,1,1,2,1,1,5,3,1,1,1,1,1,5,1,1,1,1,1,1,1,2,2,5,5,1,2,1,2,1,1,5,1,3,1,5,2,1,4,1,5,3,1,1,1,2,1,3,1,4,4,1,1,5,1,1,4,1,4,2,3,5,2,5,1,3,1,2,1,4,1,1,1,1,2,1,4,1,3,4,1,1,1,1,1,1,1,2,1,5,1,1,1,1,2,3,1,1,2,3,1,1,3,1,1,3,1,3,1,3,3,1,1,2,1,3,2,3,1,1,3,5,1,1,5,5,1,2,1,2,2,1,1,1,5,3,1,1,3,5,1,3,1,5,3,4,2,3,2,1,3,1,1,3,4,2,1,1,3,1,1,1,1,1,1]

    fish = tabulate(aoc_input)
    print(fish)

    d = 256
    fish = gen_days(fish,d)

    print("\nTotal lanternfish on day " + str(d) + ": " + str(sum(fish)))

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
