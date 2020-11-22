import math

def carparkingroof(arr, k):
    # basic checks
    if arr is None:
        return 0
    elif len(arr) < 2:
        if k == 1:
            return 1
        else:
            return 0
    elif len(arr) - k  == 0:
        return arr[k-1] - arr[0] + 1
    # sort the array incase its out of order
    arr.sort()

    mindist = math.inf
    # loop through the array with a k window and find the min distance
    for idx in range(len(arr)-k):
        if mindist > (arr[idx+k-1] - arr[idx] + 1):
            mindist = arr[idx+k-1] - arr[idx] + 1

    return mindist



if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 11, 5, 6, 7, 8]
    a3 = [2, 10, 8, 17]
    a2 = [1, 2, 3, 10]

    print(carparkingroof(a2, 4))