# https://leetcode.com/discuss/interview-question/380650/Bloomberg-or-Phone-Screen-or-Candy-Crush-1D

# use a stack or recursion

class Solution:
    def crush(self, s):
        sStk = []

        for cIdx in range(len(s)):
            char = s[cIdx]

            if len(sStk) > 0 and char == sStk[-1][0]:
                sStk[-1] = (sStk[-1][0], sStk[-1][1]+1)

            else:
                if len(sStk) > 0 and sStk[-1][1] >= 3:
                    sStk.pop(-1)
                if len(sStk) > 0 and char == sStk[-1][0]:
                    sStk[-1] = (sStk[-1][0], sStk[-1][1] + 1)
                else:
                    sStk.append((char, 1))


        res = ""
        for item in sStk:
            if not sStk[-1][1] >= 3:
                res += (item[0] * item[1])

        return res


if __name__ == '__main__':
    tester = Solution()
    ans = tester.crush("aaabbbacd")
    print(ans)
