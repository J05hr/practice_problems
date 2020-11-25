# https://leetcode.com/problems/decode-string/

# use two stacks or recursion

class Solution:

    def decodeString(self, s):
        currS = ""
        k = ""
        cStk = []
        sStk = []

        for cIdx in range(len(s)):
            char = s[cIdx]
            if char in '0123456789':
                k += char
            elif char in "[":
                cStk.append(int(k))
                sStk.append(currS)
                k = ""
                currS = ""
            elif char in "]":
                poppedS = sStk[-1]
                sStk.pop(-1)
                poppedK = cStk[-1]
                cStk.pop(-1)
                poppedS += (currS * poppedK)
                currS = poppedS
            else:
                currS += char

        return currS

    k = [""]

    def decodeString3(self, s):
        string = ""

        for cIdx in range(len(s)):
            char = s[cIdx]
            
            if char in '0123456789':
                self.k[-1] += char

            elif char in "[":
                string += self.decodeString(s[cIdx+1:])

            elif char in "]":
                if self.k[-1] != "":
                    string *= int(self.k[-1]) - 1
                    self.k.pop(-1)
                    self.k.append("")
                    return string
                
            else:
                string += char

        return string


if __name__ == '__main__':
    tester = Solution()
    ans = tester.decodeString("3[a]2[bc]")
    print(ans)
