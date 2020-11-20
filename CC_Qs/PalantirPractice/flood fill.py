"""
 An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].


https://leetcode.com/problems/flood-fill/
"""


from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """


        visited = list()
        loc = (sr, sc)

        #return self.dfsFill(image, visited, loc, newColor)
        return self.bfsFill(image, visited, loc, newColor)


    def dfsFill(self, img, visited, loc, nc):

        # approach - use recursion to perform a dfs style fill and update the pixels at the end.
        # Use a visited array to track where we've been.

        # assumptions - rectangular grid

        visited.append(loc)

        # up
        if (loc[0] - 1 in range(len(img)) and img[loc[0]][loc[1]] == img[loc[0] - 1][loc[1]] and (loc[0]-1, loc[1]) not in visited):
            self.dfsFill(img, visited, (loc[0]-1,loc[1]), nc)
            img[loc[0]-1][loc[1]] = nc


        # right
        if (loc[1] + 1 in range(len(img[0])) and img[loc[0]][loc[1]] == img[loc[0]][loc[1] + 1] and (loc[0], loc[1]+1) not in visited):
            self.dfsFill(img, visited, (loc[0],loc[1]+1), nc)
            img[loc[0]][loc[1]+1] = nc

        # down
        if (loc[0] + 1 in range(len(img)) and img[loc[0]][loc[1]] == img[loc[0] + 1][loc[1]] and (loc[0]+1, loc[1]) not in visited):
            self.dfsFill(img, visited, (loc[0]+1,loc[1]), nc)
            img[loc[0]+1][loc[1]] = nc

        # left
        if (loc[1]-1 in range(len(img[0])) and img[loc[0]][loc[1]] == img[loc[0]][loc[1]-1] and (loc[0], loc[1]-1) not in visited):
            self.dfsFill(img, visited, (loc[0],loc[1]-1), nc)
            img[loc[0]][loc[1]-1] = nc

        # done
        img[loc[0]][loc[1]] = nc
        return img



    def bfsFill(self, img, visited, loc, nc):

        # approach - use a while loop to perform a bfs style fill and update the pixels as we go.
        # Use the visited array to keep track of progress

        # assumptions - rectangular grid

        bfsQ = deque()
        bfsQ.append(loc)

        while len(bfsQ) > 0:
            cLoc = bfsQ.popleft()
            visited.append(cLoc)

            # up
            if (cLoc[0] - 1 in range(len(img)) and img[cLoc[0]][cLoc[1]] == img[cLoc[0]-1][cLoc[1]] and (
            cLoc[0]-1, cLoc[1]) not in visited):
                newLoc = (cLoc[0]-1,cLoc[1])
                bfsQ.append(newLoc)

            # right
            if (cLoc[1]+1 in range(len(img[0])) and img[cLoc[0]][cLoc[1]] == img[cLoc[0]][cLoc[1]+1] and (
            cLoc[0], cLoc[1]+1) not in visited):
                newLoc = (cLoc[0], cLoc[1]+1)
                bfsQ.append(newLoc)

            # down
            if (cLoc[0]+1 in range(len(img)) and img[cLoc[0]][cLoc[1]] == img[cLoc[0]+1][cLoc[1]] and (
            cLoc[0]+1, cLoc[1]) not in visited):
                newLoc = (cLoc[0]+1, cLoc[1])
                bfsQ.append(newLoc)

            # left
            if (cLoc[1]-1 in range(len(img[0])) and img[cLoc[0]][cLoc[1]] == img[cLoc[0]][cLoc[1]-1] and (
            cLoc[0], cLoc[1]-1) not in visited):
                newLoc = (cLoc[0], cLoc[1]-1)
                bfsQ.append(newLoc)

            img[cLoc[0]][cLoc[1]] = nc

        return img






testimage = [[1,1,1],[1,1,0],[1,0,1]]
sol = Solution()
print("floodFill")
print(sol.floodFill(testimage, 1, 1, 2))
print("\n")

