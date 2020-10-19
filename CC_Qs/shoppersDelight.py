

def shoppersDelight(pjeans, pshoes, pskirts, ptops, budget):
    # basic length check
    if 0 in [len(pjeans), len(pshoes), len(pskirts), len(ptops)]:
        return 0

    # make a matrix and a ways matrix
    mat = [pjeans, pshoes, pskirts, ptops]
    ways = []

    # basic budget check
    if budget < (pjeans[0] + pshoes[0] + pskirts[0] + ptops[0]):
        return 0

    numChoices = 0

    # loop through each item in the values matrix and update the ways array
    for idx in range(len(mat)):
        temp = []
        for idx2 in range(len(mat[idx])):
            # for the first row append a new way and the value
            if idx == 0:
                if mat[idx][idx2] <= budget:
                    temp.append(mat[idx][idx2])
                else:
                    return 0
            else:
                # add the value for all the previous ways and add any new ways
                for way in ways:
                    way += mat[idx][idx2]
                    # add if it's under budget
                    if way <= budget:
                        temp.append(way)
        ways = temp

    for way in ways:
        if way <= budget:
            numChoices += 1

    return numChoices


if __name__ == '__main__':

    a = [2, 3]
    a2 = [4]
    a3 = [2, 3]
    a4 = [1, 2]

    '''
    a = [1, 1]
    a2 = [1, 1]
    a3 = [1, 1]
    a4 = [1, 1]'''

    print(shoppersDelight(a, a2, a3, a4,  10))