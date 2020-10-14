from typing import List

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

class Solution:
    a2 = [7, 1, 5, 3, 6, 4]
    a = [1,1,2,2,3,3,4,5,5,6,6]

    def singleNumber(self, nums: List[int]) -> int:

        itemset = dict()
        for num in nums:
           if num in itemset:
               itemset.pop(num)
           else:
               itemset.setdefault(num, 1)

        res = list(itemset.keys())
        return res[0]


    def singleNumber2(self, nums: List[int]) -> int:
        nums.sort()
        idx = 0
        while idx <= len(nums)-2:
            if nums[idx] != nums[idx+1]:
                return nums[idx]
            idx += 2

memes = Solution()
print(memes.singleNumber2(memes.a))