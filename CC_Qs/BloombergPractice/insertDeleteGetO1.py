# https://leetcode.com/problems/insert-delete-getrandom-o1/

# use hybrid structure or maintain 2 structures
# if duplicates just maintain a Q or list instead of a single item
import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = list()
        self.stor = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.stor:
            self.keys.append(val)
            self.stor.setdefault(val, len(self.keys)-1)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.stor:
            data = self.stor[val]
            self.stor[self.keys[-1]] = data
            self.keys[data] = self.keys[-1]
            self.keys.pop(-1)
            self.stor.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.keys)


if __name__ == '__main__':
    tester = RandomizedSet()
    tester.insert(0)
    print(tester.keys)
    print(tester.stor)
    tester.insert(1)
    print(tester.keys)
    print(tester.stor)
    tester.remove(0)
    print(tester.keys)
    print(tester.stor)
    tester.insert(2)
    print(tester.keys)
    print(tester.stor)
    tester.remove(1)
    print(tester.keys)
    print(tester.stor)
    tester.getRandom()
    print(tester.keys)
    print(tester.stor)
