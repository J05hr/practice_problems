"""
Find The Duplicates

Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both in arr1 and arr2

Constraints:

    [time limit] 5000ms

    [input] array.integer arr1
        1 ≤ arr1.length ≤ 100

    [input] array.integer arr2
        1 ≤ arr2.length ≤ 100

    [output] array.integer
"""


class Solution:
    # if the arrays are sorted the most efficient is a simple 2 pointer walk, takes O(min(M,N)) and no extra space
    def find_duplicates(self, arr1, arr2):
        ans = []

        p1 = 0
        p2 = 0
        while p1 < len(arr1) and p2 < len(arr2):
            item = arr1[p1]
            item2 = arr2[p2]
            if item == item2:
                ans.append(item)
                p1 += 1
                p2 += 1
            elif item < item2:
                p1 += 1
            else:
                p2 += 1
        return ans

    # if the arrays are not sorted use a dictionary or a set to keep track, uses O(N) extra space
    def find_duplicates2(self, arr1, arr2):
        ans = []
        lookup = dict()
        for item in arr2:
            lookup.setdefault(item, item)

        for item2 in arr1:
            if item2 in lookup:
                ans.append(item2)
        return ans


if __name__ == '__main__':
    tester = Solution()
    ans = tester.find_duplicates(None, None)
    print(ans)
