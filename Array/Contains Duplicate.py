from typing import List

class Solution:
    a2 = [7, 1, 5, 3, 6, 4]
    a = [1, 2, 3, 4, 5, 6, 7]

    def containsDuplicate2(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        for idx in range(len(nums)):
            for idx2 in range(idx + 1, len(nums)):
                if nums[idx] == nums[idx2]:
                    return True
        return False

    def containsDuplicate3(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        a = []
        for idx in range(len(nums)):
            if nums[idx] in a:
                return True
            a.append(nums[idx])
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        nums.sort()
        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx + 1]:
                return True
        return False



memes = Solution()

print(memes.rotate(memes.a))