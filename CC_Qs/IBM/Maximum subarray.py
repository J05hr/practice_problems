"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
[-2,1,-3,4,-1,2,1,-5,4]

class Solution(object):

    # approach - add positives as we go and check against the old value to see if we need to move the start,
    #  if we come across negative we keeping check until we hit a positive then decide if its worth it to move the idxs

    # assumptions -

    def maxSub(self, nums):

        startIdx = 0
        endIdx = 0
        pV = 0
        value = 0

        # initialize value with the idx 0 information
        if len(nums) > 0:
            value = nums[0]

        # start at idx 1
        idx = 1

        # loop through the list
        while idx < len(nums):

            # calc the potential value
            if endIdx + 1 == idx:
                pV = value + nums[idx]
            else:
                pV = pV + nums[idx]

            # check if we like what we got and want to move up the ending Idx
            if pV > value:
                endIdx = idx
                value = pV

            # if we don't like what we got let's skip ahead and see if it's worth the wait
            else:
                while pV < value and pV > nums[idx] and idx < len(nums) - 1:
                    idx += 1
                    pV = pV + nums[idx]

                # now check if we like what we got and want to move up the endIdx
                if pV >= value:
                    endIdx = idx
                    value = pV
                # if its still not better lets restart the potential value from the new best looking spot
                else:
                     pV = nums[idx]

            # check if we still want all the previous stuff or if the current alone is better
            if nums[idx] >= value:
                startIdx = idx
                value = nums[idx]

            idx += 1

        answer = value
        return answer



#test = [-2,1,-3,4,-1,2,1,-5,4]
test = [8,-19,5,-4,20]
#test = [1,2,-1,-2,2,1,-2,1,4,-5,4]
sol = Solution()
print(sol.maxSub(test))











