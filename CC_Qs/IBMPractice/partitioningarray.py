import math

def partition(arr, k):
    # basic checks
    if arr is None or len(arr) < 2 or len(arr) % k != 0:
        return "No"

    # find the unique set
    itemset = list(set(arr))

    # get the max freq item
    maxfreq = 0
    for item in itemset:
        if arr.count(item) > maxfreq:
            maxfreq = arr.count(item)

    if maxfreq > len(arr)/k:
        return "No"

    return "Yes"


def partition2(arr, k):
    alen = len(arr)
    # basic checks
    if alen % k != 0:
        return "No"

    # make a dictionary for the items and map {item : count}
    itemset = dict()
    # get the max freq item
    maxfreq = 0
    for item in arr:
        try:
            itemset[item] += 1
            if itemset[item] > alen/k:
                return "No"
        except KeyError:
            itemset.setdefault(item, 1)
        if itemset[item] > maxfreq:
            maxfreq = itemset[item]

    # if we finish
    return "Yes"

if __name__ == '__main__':
    a = [1,2,3,4,5,11,5,6,7,8]
    a3 = [1, 2, 3, 4]
    a2 = [1,1,2,2,3,3,4,4,5,5,6,6]
    a4 = [x % 1000 for x in range(1000000)]
    a5 = [0,0,0,1,1,1,2,2,3,3]

    print(partition2(a4, 2))