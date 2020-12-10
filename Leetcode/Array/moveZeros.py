"""
Approach 1:
iterative
loop through, find zeros, shift them to the end using slicing
time worst case O(n)
space worst case O(n)

Approach 2:
iterative
use 2 pointers keep track of the last non-zero and then have another pointer for the next non-zero item
move all the non-zero items in after the last non-zero item, put a zero in its place, pushing all the zeros to the end
time worst case O(n)
space worst case O(1) - uses slicing for faster time, we need to copy the list references but not objects
"""


class Solution:
    def move_zeros(self, nums):
        lastIdx = -1
        curIdx = 0
        end = len(nums)
        while curIdx < end:
            num = nums[curIdx]
            if num != 0:
                nums[curIdx] = 0
                nums[lastIdx+1] = num
                lastIdx += 1
            curIdx += 1
        return nums

    def move_zeros2(self, nums):
        idx = 0
        end = len(nums)
        while idx < end:
            num = nums[idx]

            if num == 0:
                nums.pop(idx)
                nums.append(0)
                end -= 1
            else:
                idx += 1
        return nums



if __name__ == '__main__':
    tester = Solution()
    ans = tester.move_zeros([1,0,1,0])
    print(ans)
