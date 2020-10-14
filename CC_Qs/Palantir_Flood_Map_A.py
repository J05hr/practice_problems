#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'findHighPoints' function below.
#
# The function is expected to return a 2D_BOOLEAN_ARRAY.
# The function accepts 2D_INTEGER_ARRAY elevations as parameter.
#

def findHighPoints(elevations):
    bMat = list()

    rows = len(elevations)
    if rows:
        cols = len(elevations[0])

    for r in range(rows):
        bRow = list()
        for c in range(cols):

            if (r - 1 in range(rows) and elevations[r - 1][c] > elevations[r][c]):
                # not a sink
                bRow.append(0)
                continue
            if (r - 1 in range(rows) and c + 1 in range(cols) and elevations[r - 1][c + 1] > elevations[r][c]):
                # not a sink
                bRow.append(0)
                continue
            if (c + 1 in range(cols) and elevations[r][c + 1] > elevations[r][c]):
                # not a sink
                bRow.append(0)
                continue
            if (r + 1 in range(rows) and c + 1 in range(cols) and elevations[r + 1][c + 1] > elevations[r][c]):
                # not a sink
                bRow.append(0)
                continue
            if (r + 1 in range(rows) and elevations[r + 1][c] > elevations[r][c]):
                # not a sink
                bRow.append(0)
                continue
            if (r + 1 in range(rows) and c - 1 in range(cols) and elevations[r + 1][c - 1] > elevations[r][c]):
                # not a sink
                bRow.append(0)
                continue
            if (c - 1 in range(cols) and elevations[r][c - 1] > elevations[r][c]):
                # not a sink
                bRow.append(0)
                continue
            if (r - 1 in range(rows) and c - 1 in range(cols) and elevations[r - 1][c - 1] > elevations[r][c]):
                # not a sink
                bRow.append(0)
                continue

            # congrats you're a peak
            bRow.append(1)
        bMat.append(bRow)









        plataue
        def findHighPoints(elevations):
            bMat = list()

            rows = len(elevations)
            if rows:
                cols = len(elevations[0])

            for r in range(rows):
                bRow = list()
                for c in range(cols):

                    if (r - 1 in range(rows) and elevations[r - 1][c] > elevations[r][c]):
                        # not a sink
                        bRow.append(0)
                        continue
                    if (r - 1 in range(rows) and c + 1 in range(cols) and elevations[r - 1][c + 1] > elevations[r][c]):
                        # not a sink
                        bRow.append(0)
                        continue
                    if (c + 1 in range(cols) and elevations[r][c + 1] > elevations[r][c]):
                        # not a sink
                        bRow.append(0)
                        continue
                    if (r + 1 in range(rows) and c + 1 in range(cols) and elevations[r + 1][c + 1] > elevations[r][c]):
                        # not a sink
                        bRow.append(0)
                        continue
                    if (r + 1 in range(rows) and elevations[r + 1][c] > elevations[r][c]):
                        # not a sink
                        bRow.append(0)
                        continue
                    if (r + 1 in range(rows) and c - 1 in range(cols) and elevations[r + 1][c - 1] > elevations[r][c]):
                        # not a sink
                        bRow.append(0)
                        continue
                    if (c - 1 in range(cols) and elevations[r][c - 1] > elevations[r][c]):
                        # not a sink
                        bRow.append(0)
                        continue
                    if (r - 1 in range(rows) and c - 1 in range(cols) and elevations[r - 1][c - 1] > elevations[r][c]):
                        # not a sink
                        bRow.append(0)
                        continue

                    # congrats you're a peak
                    bRow.append(1)
                bMat.append(bRow)

            return bMat




















def findRiskScores(elevations):

    rows = len(elevations)
    if rows:
        cols = len(elevations[0])

    sMat = list()
    for r in range(rows):
        sRow = list()
        for c in range(cols):
            sRow.append(0)
        sMat.append(sRow)

    visited = list()

    for r in range(rows):
        for c in range(cols):

            if (r - 1 in range(rows) and elevations[r - 1][c] >= elevations[r][c]):
                continue
            if (r - 1 in range(rows) and c + 1 in range(cols) and elevations[r - 1][c + 1] >= elevations[r][c]):
                continue
            if (c + 1 in range(cols) and elevations[r][c + 1] >= elevations[r][c]):

                continue
            if (r + 1 in range(rows) and c + 1 in range(cols) and elevations[r + 1][c + 1] >= elevations[r][c]):

                continue
            if (r + 1 in range(rows) and elevations[r + 1][c] >= elevations[r][c]):

                continue
            if (r + 1 in range(rows) and c - 1 in range(cols) and elevations[r + 1][c - 1] >= elevations[r][c]):

                continue
            if (c - 1 in range(cols) and elevations[r][c - 1] >= elevations[r][c]):
                continue
            if (r - 1 in range(rows) and c - 1 in range(cols) and elevations[r - 1][c - 1] >= elevations[r][c]):
                continue

            # congrats you're a peak
            sMat = score(elevations, sMat, r, c, rows, cols, visited)
    return sMat


def score(elevations, sMat, r, c, rows, cols, visited):
        loc = (r,c)
        nbors = list()
        visited.append(loc)

        if (r - 1 in range(rows)):
            nloc = (r - 1, c)
            nbors.append(nloc)

        if (r - 1 in range(rows) and c + 1 in range(cols)):
            nloc = (r - 1, c + 1)
            nbors.append(nloc)

        if (c + 1 in range(cols)):
            nloc = (r, c + 1)
            nbors.append(nloc)

        if (r + 1 in range(rows) and c + 1 in range(cols)):
            nloc = (r + 1, c + 1)
            nbors.append(nloc)

        if (r + 1 in range(rows)):
            nloc = (r + 1, c)
            nbors.append(nloc)

        if (r + 1 in range(rows) and c - 1 in range(cols)):
            nloc = (r + 1, c - 1)
            nbors.append(nloc)

        if (c - 1 in range(cols)):
            nloc = (r, c - 1)
            nbors.append(nloc)

        if (r - 1 in range(rows) and c - 1 in range(cols)):
            nloc = (r - 1, c - 1)
            nbors.append(nloc)

        for nloc in nbors:
            if nloc not in visited and elevations[nloc[0]][nloc[1]] < elevations[r][c]:
                sMat[r][c] += 1
                score(elevations, sMat, nloc[0], nloc[1], rows, cols, visited)

        return sMat








test = [[1, 2, 1, 3, 4],

[1, 5, 2, 2, 2],

[4, 5, 1, 9, 7],

[3, 5, 3, 7, 6],

[4, 3, 1, 7, 3]]

print(findRiskScores(test))



































