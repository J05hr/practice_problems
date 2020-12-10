"""
Approach:
iterative
attempt to add one to the least significant digit,
otherwise "carry" by zeroing out the digit and attempt to add to the next digit

time worst case O(2n)
space worst case O(1) - in place
"""


class Solution:
    def plus_one(self, digits):
        # loop through the digits starting with with the least significant
        for idx in reversed(range(len(digits))):
            # if the digit is 9 we need to carry
            if digits[idx] == 9:
                # zero out the 9
                digits[idx] = 0
                # if we need to carry at the zero index then we need to add a new 1 digit
                if idx == 0:
                    digits.insert(0, 1)
            # otherwise we can just add one and break
            else:
                digits[idx] += 1
                break

        return digits



if __name__ == '__main__':
    tester = Solution()
    ans = tester.plus_one([9])
    print(ans)
