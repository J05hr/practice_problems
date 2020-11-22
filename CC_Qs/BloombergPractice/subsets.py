# https://leetcode.com/problems/subsets


class Solution:
    def subsets(self, nums):
        # results array
        res = list()
        # always add an empty subset
        res.append([])
        # return on empty array or singleton
        if len(nums) == 0:
            return res
        if len(nums) == 1:
            return res.append(nums[0])

        for item in nums:
            subsetarr = []

        return res



if __name__ == '__main__':
    tester = Solution()
    ans = tester.subsets([1,2,3])
    print(ans)