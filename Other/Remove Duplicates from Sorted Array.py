from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0

        if len(nums) == 0:
            return count
        else:
            for idx in range(len(nums)):

                count += 1

                if idx == len(nums) - 1:
                    return count

                while nums[idx] == nums[idx + 1]:

                    nums.pop(idx + 1)

                    if idx == len(nums) - 1:
                        return count
