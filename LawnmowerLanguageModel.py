# just chewing up a text and generating nonsense based on it

import random

def process(book,depth):
    dip = depth

    seeds = []
    leaves = []

    while len(book) >= depth:
        slab = book[:dip]

        if slab in seeds:
            leaves[seeds.index(slab)].append(book[dip])
        else:
            seeds.append(slab)
            leaves.append([book[dip]])

        book = book[dip:]

    return seeds, leaves


def get_opts(seeds,leaves,input):
    print(input)
    if input not in seeds:
        return []
    else:
        return leaves[seeds.index(input)]


def generate(seeds,leaves,start,length):
    cursor = start[-3:]

    slab = ""

    while len(slab) < 500:
        opts = get_opts(seeds,leaves,cursor)
        print(opts)
        if opts:
            next = random.choice(opts)
        else:
            next = "j"
        slab += next
        cursor = slab[-3:]
        print(slab)

    return slab


if __name__ == "__main__":


    depth = 3


    f = open('/home/robynskyrme/mobydick.txt')
    book = f.read()
    f.close()

    book = book.replace("\n", " ")

    book = book[:70000]

    seeds, leaves = process(book,depth)

    text = generate(seeds,leaves,"MOB",500)

    print(text)