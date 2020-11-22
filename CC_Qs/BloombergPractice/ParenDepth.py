# find string at highest depth e.g.,((AB)(((CD)))) return depth 4 and string = CD


class Solution:
    def deepString(self, s):

        res = ""

        if len(s) < 2:
            return res

        stack = []
        pair = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in "({[":
                stack.append(char)
                res += char
            elif char in ")}]":
                if len(stack) != 0:
                    if stack[-1] == pair[char]:
                        stack.pop(-1)
                        res += char
            else:
                res += char

        return res


if __name__ == '__main__':
    tester = Solution()
    ans = tester.deepString("((AB)(((CD))))")
    print(ans)
