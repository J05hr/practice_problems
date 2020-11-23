# https://leetcode.com/problems/palindrome-number/
import math

class Solution:
    def pal(self, num):
        # neg arent palandromes
        if num < 0:
            return False
        elif num == 0:
            return True
        else:
            digits = math.floor(math.log10(num)+1)
            # use modulo or bitmasks to get individual digits
            # Go through the last half of the digits find their values and check against opposite digit
            backNum = num
            frontNum = num
            halfidx = math.ceil(digits/2)
            for digit in range(1, halfidx+1):
                # get the first digit and remove
                val = backNum % 10
                backNum = math.floor(backNum/10)
                # calc the op digit loc
                opDigit = digits - digit + 1
                # use division to get the opVal
                opMask = pow(10, opDigit-1)
                opVal = math.floor(frontNum / opMask)
                frontNum = frontNum % opMask
                # compare
                if val != opVal:
                    return False
        return True


if __name__ == '__main__':
    tester = Solution()
    ans = tester.pal(1991)
    print(ans)
