
"""
Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.
Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).
Explain and code the most efficient solution possible, and analyze its time and space complexities.
Example:
input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)

Constraints:
[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer s

[output] array.integer
"""


class Solution:
    def findArrayQuadruplet(self, arr, s):
        n = len(arr)

        # if there are fewer than 4 items in arr, by
        # definition no quadruplet exists whose sum is s
        if n < 4:
            return []

        # sort arr in an ascending order
        arr.sort()

        for idx in range(n-3):
            for idx2 in range(idx + 1, n-2):
                # trgt stores the complementing sum
                trgt = s - (arr[idx] + arr[idx2])

                # check for the trgt in subarray arr[j+1…n-1]
                high = n - 1
                low = idx2 + 1

                while low < high:
                    if arr[low] + arr[high] < trgt:
                        low += 1
                    elif arr[low] + arr[high] > trgt:
                        high -= 1
                    # quadruplet with given sum found
                    else:
                        return [arr[idx], arr[idx2], arr[low], arr[high]]
        return []

    def findArrayQuadruplet2(self, arr, s):
        n = len(arr)
        # if there are fewer than 4 items there cant be a 4sum
        if n < 4:
            return []
        # sort arr in an ascending order
        arr.sort()

        for idx in range(n-3):
            for idx2 in range(idx+1, n-2):
                for idx3 in range(idx+2, n-1):
                    for idx4 in range(idx+3, n):
                        if arr[idx] + arr[idx2] + arr[idx3] + arr[idx4] == s:
                            return [arr[idx], arr[idx2], arr[idx3], arr[idx4]]
        return []

    def findArrayQuadruplet3(self, arr, s):

        quads = []
        temp_quads = []
        seen = set()

        # if there are fewer than 4 items there cant be a 4sum
        if len(arr) < 4:
            return []

        # sort arr in an ascending order
        arr.sort()

        for a in arr:
            qidx = 0
            while qidx < len(quads):
                quad = quads[qidx]
                quad.append(a)
                # found full quad
                if len(quad) == 4:
                    # return if sum found
                    if sum(quad) == s:
                        return quad
                    # if not mutate into new quads and pop the old one
                    else:
                        if quad[0] not in seen:
                            seen.add(quad[0])
                            temp_quads.append([quad[0]])
                            temp_quads.append([quad[0], quad[1]])
                            temp_quads.append([quad[0], quad[2]])
                            temp_quads.append([quad[0], quad[3]])
                            temp_quads.append([quad[0], quad[1], quad[2]])
                            temp_quads.append([quad[0], quad[1], quad[3]])
                            temp_quads.append([quad[0], quad[2], quad[3]])
                        else:
                            temp_quads.append(quad[:-3])
                            temp_quads.append(quad[:-2])
                            temp_quads.append(quad[:-1])
                        quads.pop(qidx)
                        qidx -= 1
                qidx += 1
            quads.append([a])
            quads.extend(temp_quads)
            temp_quads = []
        return []


if __name__ == '__main__':
    tester = Solution()
    ans = tester.findArrayQuadruplet3([2, 7, 4, 0, 9, 5, 1, 3], 20)
    print(ans)
