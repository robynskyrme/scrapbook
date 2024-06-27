# TERNE
# ‘What should I do now?’
#
# A very simple program to help me get through my day, one suggestion at a time.
# No clutter. Some prioritization.


# 27.6.2024 --- reads file, builds deck, shuffles it with relative heft of tasks,
#               suggests tasks when prompted until all tasks have been suggested
#
#               tomorrow: comment this code, please



import random

class card:
    def __init__(self, task, heft):
        self.task = task
        self.heft = heft


deck = []
shuffle = []
rs = 19

# a task given '0' heft ("I don't know") will be assigned the mean of all explicitly hefted tasks, divided by THIS number:
# (larger number here therefore means less likely)
zeroweight = 3

def read_deck(filename):
    with open(filename) as file:
        for line in file:
            deck.append(line_to_card_split(line))


def line_to_card_split(line):
    char = ""
    heftstr = ""
    while char != " ":
        char = line[-1]
        heftstr = char + heftstr
        line = line[:-1]

    heftstr = heftstr[1:]

    newcard = card(line,int(heftstr))
    return newcard

def avg_zeroes():
    nonzerosum = 0
    nonzerocount = 0
    for card in deck:
        if card.heft > 0:
            nonzerosum += card.heft
            nonzerocount += 1
    if nonzerosum == 0:
        for card in deck:
            card.heft = 1
        return

    nonzerosum = int((nonzerosum / nonzerocount)/zeroweight)

    for card in deck:
        if card.heft == 0:
            card.heft = nonzerosum

def build_shuffle():
    for card in range(len(deck)):
        for heft in range(deck[card].heft):
            shuffle.append(card)


def suggest():
    shufflesize = len(shuffle)
    pickacard = random.randint(0,shufflesize-1)
    return deck[shuffle[pickacard]].task

def print_deck():
    for card in deck:
        print("TASK: " + card.task + " with heft of " + str(card.heft))

def inputloop():
    userinput = ""
    alreadysuggested = []

    while userinput == "":
        task = suggest()
        while task in alreadysuggested:
            task = suggest()
        alreadysuggested.append(task)
        print("SUGGESTION:")
        print(task)
        if len(alreadysuggested) == len(deck):
            return
        userinput = input()


if __name__ == "__main__":

    read_deck("terne_deck001.txt")
    #deck.append(line_to_card_split("Fox Fox Fox! 73"))

    avg_zeroes()

    #'print_deck()

    build_shuffle()

    inputloop()

    print("\nALL TASKS SUGGESTED")