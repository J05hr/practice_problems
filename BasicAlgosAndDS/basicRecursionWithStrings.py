
class Solution:
    def reverseString(self, s) -> None:

        def recrev(s, idx, stop):
            if idx >= stop - 1:
                return s
            else:
                idx += 1
                return [s[-1]].append(recrev((s[:-1]), idx, stop))

        idx = 0
        stop = len(s)
        s = recrev(s, idx, stop)


if __name__ == '__main__':
    tester = Solution()
    ans = "String"
    tester.reverseString("String")
    print(ans)