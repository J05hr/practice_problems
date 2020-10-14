import math

def separatingstudents(n, students):

    moves = 0

    # basic checks
    if len(students) < 3:
        return moves

    countzeros = students.count(0)
    if countzeros == 0 or countzeros == len(students):
        return moves

    # check and set the optimal sort
    # tuple contains the optimal value to come first and the count of that value
    order = (0, countzeros)
    countones = len(students) - countzeros
    halfidx = math.ceil((len(students)-1)/2)
    if students[:halfidx].count(0) < math.ceil(countzeros)/2:
        order = (1, countones)

    # check for already sorted
    if students[:halfidx].count(order[0]) == order[1]:
        return 0

    # count moves
    lastidx = 0
    for movedstudent in range(order[1]):
        curidx = students.index(order[0], lastidx)
        moves += curidx - movedstudent
        lastidx = curidx + 1

    return moves


if __name__ == '__main__':
    n = 8
    a = [1, 0, 1, 1, 0, 1, 1]
    print(separatingstudents(n, a))