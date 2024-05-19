# 17.5.2024
# Finding a formula for the lengths of the months
# The first 5 terms of 7x-5 gives the correct months once each (if labelled 1-12)
# lists those months from which 1 should be subtracted from 31
# -- but I want to find a formula which includes February 3 times. Or, twice, on leap years

def months(start,inc):
    lengths = []
    for a in range(5):
        lengths.append(start % 12)
        start += inc
    return lengths



def MergeSort(list):


    # the base case: a string of length 1 is already sorted, so return it
    if len(list) == 1:
        return list

        # create a list which the halves will be merged into
    result = []

    # integer that splits the list in two (exactly if even, lopsided if list is odd)
    half = int(len(list) / 2)

    # recursion: both halves are themselves merge-sorted
    left = MergeSort(list[:half])
    right = MergeSort(list[half:])

    # a count of elements, for the following while loop
    total = len(left) + len(right)
    # while elements remain, merge the lists one element at a time
    while len(result) < total:
        if left and right:
            # case for two elements equal (just take the left)
            if left[0] == right[0]:
                result.append(left[0])
                left = left[1:]
        if left and right:
            # cases for two elements that differ
            if left[0] < right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
                # cases when one of the lists has been emptied
        if left and not right:
            result.append(left[0])
            left = left[1:]
        if right and not left:
            result.append(right[0])
            right = right[1:]

            # return the merged list
    return result



if __name__ == "__main__":

    for a in range (1000000):
        lengths = months(2,a)
        lengths = MergeSort(lengths)
        if lengths == [2,2,2,4,6,9,11]:
            print(lengths)


