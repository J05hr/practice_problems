import math

def triplets(n, nums, thres):

    # sort the list and make sure it's a unique set
    nums = list(set(nums))
    nums.sort()

    # add the first two numbers to get the window ending value
    windowendvalue = thres - (nums[0] + nums[1])

    # use dp by saving results to another list so we don't recalculate each time
    ways = 0
    triplets = []
    overshot = []

    # loop through all the nums
    for numidx in range(len(nums)):

        # shorten the list based on sanity
        if nums[numidx] > windowendvalue:
            break

        # if any are over on the last pass remove them
        for tripid in overshot:
            triplets.pop(tripid)
        overshot.clear()

        # for each num loop through an array of triplets and add it if possible
        for tripidx in range(len(triplets)):
            # otherwise add the number into any existing triplets and make a new one
            # if you come across a full triplet after adding then check it and add to ways count
            # if less than threshold, mutate into two triplets 0,1 and 0,2 as branch possibilities, otherwise pop it out
            triplets[tripidx].append(nums[numidx])
            if len(triplets[tripidx]) == 3:
                if triplets[tripidx][0] + triplets[tripidx][1] + triplets[tripidx][2] <= thres:
                    ways += 1
                    if [triplets[tripidx][0], triplets[tripidx][2]] not in triplets:
                        triplets.append([triplets[tripidx][0], triplets[tripidx][2]])
                    triplets[tripidx].pop(2)
                else:
                    overshot.append(tripidx)


        # make a new triplet for the number
        triplets.append([nums[numidx]])

    return ways


if __name__ == '__main__':
    n = 0
    a = [1, 2, 3, 4, 5]
    t = 11
    print(triplets(n, a, t))