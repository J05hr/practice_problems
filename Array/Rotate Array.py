from typing import List

class Solution:
    a2 = [7, 1, 5, 3, 6, 4]
    a = [1, 2, 3, 4, 5, 6, 7]


    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for rnd in range(k):
            sv = 0
            for idx in range(len(nums)):
                if idx == 0:
                    sv = nums[idx]
                    nums[idx] = nums[len(nums) - 1]
                else:
                    temp = nums[idx]
                    nums[idx] = sv
                    sv = temp

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nah bb chill
        if k >= len(nums):
            k = k % len(nums)

        if k != 0 and len(nums) > 1:

            # count loopidx
            loopidx = 0

            # do zero first
            idx = 0
            sv = nums[idx + k]
            nums[idx + k] = nums[idx]
            idx += k

            for move in range(len(nums) - 1):

                # if we are back due to odd or even split then move and restart
                if idx == loopidx:
                    idx += 1
                    loopidx += 1
                    sv = nums[idx + k]
                    nums[idx + k] = nums[idx]
                    idx += k

                # case we are looping around
                elif idx + k >= len(nums):
                    nxtidx = k - (len(nums) - idx)
                    temp = nums[nxtidx]
                    nums[nxtidx] = sv
                    sv = temp
                    idx = nxtidx

                # all other moves
                else:
                    temp = nums[idx + k]
                    nums[idx + k] = sv
                    sv = temp
                    idx += k


memes = Solution()

print(memes.rotate(memes.a, 3))