"""
Matrix Spiral Copy

Given a 2D array (matrix) inputMatrix of integers, create a function spiralCopy that copies inputMatrix’s values into a 1D array in a spiral order, clockwise. Your function then should return that array. Analyze the time and space complexities of your solution.

Example:

input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

See the illustration below to understand better what a clockwise spiral order looks like.

alt Clockwise spiral order

Constraints:

    [time limit] 5000ms

    [input] array.array.integer inputMatrix
        1 ≤ inputMatrix[0].length ≤ 100
        1 ≤ inputMatrix.length ≤ 100

    [output] array.integer
"""


class Solution:

    def spiral_copy(self, input_matrix):

        res = list()
        rows = 0
        rowe = len(input_matrix)
        cols = 0
        cole = len(input_matrix[0])

        while rows < rowe and cols < cole:

            # we have rowstart. iterate the col
            for idx in range(cols, cole):
                res.append(input_matrix[rows][idx])
            rows += 1  # 1,2,3,4,5

            for idx in range(rows, rowe):
                res.append(input_matrix[idx][cole - 1])  # 10,15,20
            cole -= 1

            if rows < rowe:
                for idx in range(cole - 1, cols - 1, -1):
                    res.append(input_matrix[rowe - 1][idx])
            rowe -= 1  # 1,2,3,4,5

            if cols < cole:
                for idx in range(rowe - 1, rows - 1, -1):
                    res.append(input_matrix[idx][cols])  # 10,15,20
            cols += 1

        return res


if __name__ == '__main__':
    tester = Solution()
    ans = tester.spiral_copy([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
    print(ans)
