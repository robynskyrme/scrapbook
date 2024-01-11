
# 15.3.2023
# "Machine learning" lol
#
# Approach: having told it what the words for 0-9 are,
# make it try to spell them, letter by letter, guessing from an intially rubbish list of letters (i.e. one random letter);
# then, have it repeatedly guess letters, and if a letter is correct, add it to the list of possibilities for that letter
# such that the chance of guessing that letter correctly slooooowly approaches 1
#
# Variable in __main__ called repeat_test is the threshold for "how many times has it got it 100% right in a row"
# -- it stops when it's reached this count
#
# For attention:
# -- get a real intuition for how counting _works_ in while and for loops;
#       _where_ in the loops (before or after their activity) outputs and alterations must sit
# -- split out into many more methods to make it customizable outside of the initial digit-words idea
# -- consider how to recognize when an aspect of a guess is _probably right_, in particular
#       when it has arrived (and it does so fairly quickly) at the idea that a word is a certain length
#       (that is, the rightmost characters are mostly spaces)
#

import random
#import time

one_to_nine = []

words_to_nine = []
words_to_nine.append("zero ")
words_to_nine.append("one  ")
words_to_nine.append("two  ")
words_to_nine.append("three")
words_to_nine.append("four ")
words_to_nine.append("five ")
words_to_nine.append("six  ")
words_to_nine.append("seven")
words_to_nine.append("eight")
words_to_nine.append("nine ")


def create_one_to_nine_list():
    for n in range (10):
        one_to_nine.append([])
        for c in range(5):
            one_to_nine[n].append([])
            one_to_nine[n][c].append(chr(random.randint(0,25)+97))


def word_for_n(n):
    word = ""
    for c in range(5):
        r = random.randint(0,len(one_to_nine[n][c])-1)
        #print("Number is: " +str(n))
        #print("c is " + str(c))
        #print("r is " + str(r))
        #print(one_to_nine[n][c])
        char = one_to_nine[n][c][r]
        if ord(char) > 96:
            word = word + one_to_nine[n][c][r]
        else:
            word = word + " "
        #print(word)

    return word


def output_one_to_nine():
    slab = ""
    for n in range(9):
        slab = slab + word_for_n(n).strip() + " "
        #print(str(n) + ": " + word_for_n(n)) # + " = " + words_to_nine[n])
        #print(word_for_n(n))
        #word_for_n(n)
    slab = slab + word_for_n(9).strip()
    #print(slab)
    return slab

def learn_letters(new_string):
    #print(new_string)
    for number in range(10):
        #print(number)
        for letter in range(5):
            #print(letter)
            if new_string[letter] == 0:
                char = " "
            else:
                char = chr(new_string[letter]+97)
                #print(char)
            #print(words_to_nine[number][letter])
            if char == words_to_nine[number][letter]:
                #print(words_to_nine[number][letter])
                one_to_nine[number][letter].append(char)


#        print(str(number) + ": " + str(occurrences))

if __name__ == "__main__":

    create_one_to_nine_list()

    output_one_to_nine()

    number = 0

                            # Threshold for correct guesses in a row
    repeat_test = 5

    repeats = 1
    attempts = 0

    while repeats < repeat_test:

        #time.sleep(0.1)

        attempts += 1

        new_string = []
        for k in range(5):
            new_string.append(random.randint(0,26))
                # for j in range(5):
                #     new_string.append(0)

        learn_letters(new_string)

        test_output = output_one_to_nine()


                            # This line to be un-commented to see every stage
        print(test_output)

        if test_output != "zero one two three four five six seven eight nine":

            last_hit = False
            repeats = 0
        else:
            repeats += 1
            if last_hit == False:
                repeats = 1

            last_hit = True

        #print(repeats)

    print("\nArrived at correct words " + str(repeat_test) + " times in a row after " + str(attempts) + " iterations:")
    print(test_output)

    #print(one_to_nine)





