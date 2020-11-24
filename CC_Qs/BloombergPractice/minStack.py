# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.minItem = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minItem is None or x < self.minItem:
            self.minItem = x

    def pop(self) -> None:
        deleted = self.top()
        self.stack.pop(-1)
        if deleted == self.minItem:
            self.minItem = min(self.stack, default=None)

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.minItem


if __name__ == '__main__':
    obj = MinStack()
    obj.push(2)
    obj.push(0)
    obj.push(3)
    obj.push(0)
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
