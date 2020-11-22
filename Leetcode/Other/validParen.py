def isValid(self, s: str) -> bool:
    if len(s) < 2:
        return False

    stack = []
    pair = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if len(stack) == 0:
                return False

            if stack[-1] == pair[char]:
                stack.pop(-1)
            else:
                return False

        else:
            return False

    if len(stack) > 0:
        return False

    return True