# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# sliding window

class Solution:
    def lSubstring(self, s):
        leng = len(s)
        curL = dict()
        maxC = 0
        srt = 0
        for cIdx in range(leng):
            char = s[cIdx]
            # look ahead check and add to set
            if char not in curL:
                curL.setdefault(char, cIdx + 1)
            else:
                srt = max(srt, curL[char])
                curL[char] = cIdx + 1
            maxC = max(maxC, (cIdx - srt + 1))
        return maxC


    def lSubstring2(self, s):
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}
        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans


if __name__ == '__main__':
    tester = Solution()
    ans = tester.lSubstring("abcabcbb")
    print(ans)
