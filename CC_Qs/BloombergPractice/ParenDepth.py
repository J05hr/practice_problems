# find string at highest depth e.g.,((AB)(((CD)))) return depth 4 and string = CD


class Solution:
    def deepString(self, s):

        res = ""
        maxd = 0

        if len(s) < 2:
            return res

        stack = []
        pair = {')': '(', '}': '{', ']': '['}

        depth = 0
        temp = ""
        for charIdx in range(len(s)):
            char = s[charIdx]
            if char in "({[":
                temp = ""
                stack.append((char, charIdx))
                depth += 1
                if maxd < depth:
                    maxd = depth
            elif char in ")}]":
                if len(stack) != 0:
                    if stack[-1][0] == pair[char]:
                        stack.pop(-1)
                        if depth == maxd:
                            res = temp
                        depth -= 1
            else:
                temp += char

        return res


if __name__ == '__main__':
    tester = Solution()
    ans = tester.deepString("((AB)(((CD))))")
    print(ans)
