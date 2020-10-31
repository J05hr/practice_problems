class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def recrev(s, idx, stop):
            if idx >= stop - 1:
                return s
            else:
                idx += 1
                return [s[-1]].append(recrev((s[:-1]), idx, stop))

        idx = 0
        stop = len(s)
        s = recrev(s, idx, stop)


memes = Solution()

a1 = ["h", "e", "l", "l", "o"]

print(memes.reverseString(a1))