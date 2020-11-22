# https://leetcode.com/problems/valid-anagram/

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    tdic = dict()
    sdic = dict()

    for char in t:
        try:
            tdic[char] += 1
        except KeyError:
            tdic.setdefault(char, 1)

    for char in s:
        try:
            sdic[char] += 1
        except KeyError:
            sdic.setdefault(char, 1)

    for char in tdic:
        try:
            if sdic[char] != tdic[char]:
                return False
        except KeyError as e:
            return False
    return True


def isAnagram2(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    tdic = dict()

    for char in t:
        try:
            tdic[char] += 1
        except KeyError:
            tdic.setdefault(char, 1)

    for char in s:
        if char in tdic:
            if tdic[char] <= 0:
                return False
            else:
                tdic[char] -= 1
        else:
            return False
    return True
