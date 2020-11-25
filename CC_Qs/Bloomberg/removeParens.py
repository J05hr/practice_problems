# https://leetcode.com/discuss/interview-question/124551/
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def minRemoveToMakeValid(self, s):

        if len(s) < 2:
            return ""

        stack = []
        pair = {')': '(', '}': '{', ']': '['}

        for charIdx in range(len(s)):
            char = s[charIdx]
            if char in "({[":
                stack.append((char, charIdx))
            elif char in ")}]":
                if len(stack) != 0:
                    if stack[-1][0] == pair[char]:
                        stack.pop(-1)
                    else:
                        stack.append((char, charIdx))
                else:
                    stack.append((char, charIdx))

        res = list(s)
        pops = 0
        for leftover in reversed(stack):
            res.pop(leftover[1]-pops)

        ans = ""
        return ans.join(res)


if __name__ == '__main__':
    tester = Solution()
    # ans = tester.minRemoveToMakeValid("lee(t(c)o)de)")
    ans2 = tester.minRemoveToMakeValid("))((")
    print(ans2)
