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
