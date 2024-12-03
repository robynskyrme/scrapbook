# 1,2,3,4...
# interleave with sums e.g. 1,3,2,5,3,7,4...

def stretchsum(n,iter): # integer n, taken to n iterations
    list = []
    for a in range(n):
        list.append(a+1)

    if iter > n:
        iter = n

    if iter == 1:
        return list

    for i in range(iter-1):
        stretch(list)


    return list


def stretch(list):
    index = len(list)-1
    while index > 0:
        list.insert(index,list[index]+list[index-1])
        index -= 1
    return list

if __name__ == "__main__":
    for n in range(19):
        j = stretchsum(n,n) # (4,4) should return 205
        #print(j)
        print(sum(j))