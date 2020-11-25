# https://leetcode.com/problems/3sum/



class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                seen = set()
                j = i + 1
                while j < len(nums):
                    complement = -nums[i] - nums[j]
                    if complement in seen:
                        res.append([nums[i], nums[j], complement])
                        while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                            j += 1
                    seen.add(nums[j])
                    j += 1
        return res

    def threeSum2(self, nums):
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res
