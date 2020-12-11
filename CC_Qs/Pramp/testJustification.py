# https://leetcode.com/problems/text-justification/
"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""

class Solution:

    def fullJustify(self, words, maxWidth):

        words.append("end")
        lines = list()
        tempLine = list()
        curLen = 0
        idx = 0

        while idx < len(words):
            curWord = words[idx]

            # first line item
            if len(tempLine) == 0 and curWord != "end":
                tempLine.append(curWord)
                curLen += len(curWord)
                idx += 1
            # next line items
            elif len(curWord) + curLen + len(tempLine) <= maxWidth and curWord != "end":
                tempLine.append(curWord)
                curLen += len(curWord)
                idx += 1
            # record line and start new line
            else:
                fill = maxWidth - curLen
                # regular line
                if curWord != "end":
                    sper = int(fill / ((len(tempLine) - 1) or 1))
                    extra = fill % ((len(tempLine) - 1) or 1)
                    line = ""
                    for tidx in range(len(tempLine)):
                        word = tempLine[tidx]
                        sp = " " * sper
                        if tidx == 0:
                            if len(tempLine) == 1:
                                if extra != 0:
                                    sp += " "
                                    extra -= 1
                                line += word + sp
                            else:
                                line += word
                        else:
                            if extra != 0:
                                sp += " "
                                extra -= 1
                            line += sp + word
                    lines.append(line)
                # last line
                else:
                    line = ""
                    for tidx in range(len(tempLine)):
                        word = tempLine[tidx]
                        if tidx == 0:
                            line += word
                        else:
                            line += " " + word
                            fill -= 1
                    line += " " * fill
                    lines.append(line)
                    idx += 1
                tempLine = list()
                curLen = 0

        return lines


if __name__ == '__main__':
    tester = Solution()
    ans = tester.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    ans2 = tester.fullJustify( ["What", "must", "be", "acknowledgment", "shall", "be"], 16)
    print(ans2)


