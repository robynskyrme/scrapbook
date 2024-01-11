# 3.3.2023
#
# Experiment with assigning unique values to words based on their letters
# (essentially every word treated as a number in base 26)

    # Return a number from 1-26
def get_alph(letter):
    return ord(letter)-96


def assign_value(word):

    value = 0

    for countback in range(len(word),0,-1):
        letter_placevalue = (len(word)-countback)
        print (letter_placevalue)
        # Value 0-25 of individual letter
        letterval = get_alph(word[countback-1])
        value = value + letterval*(26**letter_placevalue)

    return value







    # Take input
if __name__ == '__main__':
    word = " "
    while word != "":
        word = input("Word: ")
        print(assign_value(word))