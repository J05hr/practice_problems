"""
A group of farmers has some elevation data, and we’re going to help them understand how rainfall flows over their farmland.
We’ll represent the land as a two-dimensional array of altitudes and use the following model, based on the idea that water flows downhill:

If a cell’s four neighboring cells all have higher altitudes, we call this cell a sink; water collects in sinks.
Otherwise, water will flow to the neighboring cell with the lowest altitude. If a cell is not a sink, you may assume it has a unique lowest neighbor and that this neighbor will be lower than the cell.

Cells that drain into the same sink – directly or indirectly – are said to be part of the same basin.

Your challenge is to partition the map into basins. In particular, given a map of elevations, your code should partition the map into basins and output the sizes of the basins, in descending order.

Assume the elevation maps are square. Input will begin with a line with one integer, S, the height (and width) of the map. The next S lines will each contain a row of the map, each with S integers – the elevations of the S cells in the row. Some farmers have small land plots such as the examples below, while some have larger plots. However, in no case will a farmer have a plot of land larger than S = 5000.

Your code should output a space-separated list of the basin sizes, in descending order. (Trailing spaces are ignored.)

While correctness and performance are the most important parts of this problem, a human will be reading your solution, so please make an effort to submit clean, readable code. In particular, do not write code as if you were solving a problem for a competition.

A few examples are below.

Input:
3
1 5 2
2 4 7
3 6 9
Output:
7 2
The basins, labeled with A’s and B’s, are:
A A B
A A B
A A A


Input:
1
10
Output:
1


Input:
5
1 0 2 5 8
2 3 4 7 9
3 5 7 8 9
1 2 5 4 2
3 3 5 2 1
Output:
11 7 7
The basins, labeled with A’s, B’s, and C’s, are:
A A A A A
A A A A A
B B A C C
B B B C C
B B C C C


Input:
4
0 2 1 3
2 1 0 4
3 3 3 3
5 5 2 1 
Output:
7 5 4
"""




class Solution(object):

    def basins(self, grid, size):

        # approach - for each index check if its a sink, then from the sink, recursive dfs for flow path, check the neighbors against parent value to distinguish flow from ridges or peaks.

        # assumptions - square grid

        basinsizes = list()

        for r in range(size):
            for c in range(size):

                if (r-1 in range(size) and grid[r-1][c] < grid[r][c]):
                    # not a sink
                    continue
                if (c+1 in range(size) and grid[r][c+1] < grid[r][c]):
                    # not a sink
                    continue
                if (r+1 in range(size) and grid[r+1][c] < grid[r][c]):
                    # not a sink
                    continue
                if (c-1 in range(size) and grid[r][c-1] < grid[r][c]):
                    # not a sink
                    continue

                # congrats you're a sink
                visited = list()
                count = 0
                basinsizes.append(self.dfsCount(grid,r,c,size,visited,count,grid[r][c]))

        basinsizes.sort(reverse=True)
        print(basinsizes)


    def dfsCount(self, grid, r, c, size, visited, count, parentValue):
        loc = (r,c)
        nbors = list()

        if r - 1 in range(size):
            nloc = (r-1,c)
            nbors.append(nloc)

        if c + 1 in range(size):
            nloc = (r, c+1)
            nbors.append(nloc)

        if r + 1 in range(size):
            nloc = (r+1, c)
            nbors.append(nloc)

        if c - 1 in range(size):
            nloc = (r, c-1)
            nbors.append(nloc)

        # if there are any neighbors smaller than the parentValue the current cell will not be part of this basin
        for nloc in nbors:
            if (parentValue > grid[nloc[0]][nloc[1]]):
                    return count + 0

        visited.append(loc)

        for nloc in nbors:
            if nloc not in visited and grid[nloc[0]][nloc[1]] > grid[r][c]:
                count = self.bfsCount(grid, nloc[0], nloc[1], size, visited, count, grid[r][c])


        return count + 1









testimage = [[1,0,2,5,8], [2,3,4,7,9], [3,5,7,8,9], [1,2,5,4,2], [3,3,5,2,1]]
#testimage = [[0,3,8], [3,5,7], [1,2,0]]
sol = Solution()
print("Basins")
sol.basins(testimage, 5)
print("\n")