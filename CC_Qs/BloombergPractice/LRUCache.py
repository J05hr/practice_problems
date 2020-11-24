# https://leetcode.com/problems/lru-cache/
import time
from collections import OrderedDict

# also can use python dict and doubely LL or list



class LRUCache:

    def __init__(self, capacity: int):
        self.keys = list()
        self.sdict = dict()
        if capacity > 0:
            self.cap = capacity
        else:
            raise Exception("Invalid Capacity")

    def get(self, key: int) -> int:
        if key in self.sdict:
            data = self.sdict[key]
            self.keys.pop(data[1])
            self.keys.append(key)
            return data[0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.sdict:
            data = self.sdict[key]
            self.keys.pop(data[1])
            self.keys.append(key)
            self.sdict[key] = (value, len(self.keys) - 1)
        else:
            if len(self.keys) == self.cap:
                self.sdict.pop(self.keys[0])
                self.keys.pop(0)

            self.keys.append(key)
            self.sdict.setdefault(key, (value, len(self.keys)-1))





class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)




if __name__ == '__main__':
    test = LRUCache(2)
    test.get(2)
    print(test.keys)
    print(test.sdict)
    test.put(2, 6)
    print(test.keys)
    print(test.sdict)
    test.get(1)
    print(test.keys)
    print(test.sdict)
    test.put(1, 5)
    print(test.keys)
    print(test.sdict)
    test.put(1, 2)
    print(test.keys)
    print(test.sdict)
    test.get(1)
    print(test.keys)
    print(test.sdict)
    test.get(2)
    print(test.keys)
    print(test.sdict)
    """test = LRUCache(2)
    test.put(1, 1)
    print(test.keys)
    print(test.sdict)
    test.put(2, 2)
    print(test.keys)
    print(test.sdict)
    test.get(1)
    print(test.keys)
    print(test.sdict)
    test.put(3, 3)
    print(test.keys)
    print(test.sdict)
    test.get(2)
    print(test.keys)
    print(test.sdict)
    test.get(3)
    print(test.keys)
    print(test.sdict)
    test.put(4, 4)
    print(test.keys)
    print(test.sdict)
    test.get(1)
    print(test.keys)
    print(test.sdict)
    test.get(3)
    print(test.keys)
    print(test.sdict)
    test.get(4)
    print(test.keys)
    print(test.sdict)
    test = LRUCache(2)
    test.put(2, 1)
    print(test.keys)
    print(test.sdict)
    test.put(2, 2)
    print(test.keys)
    print(test.sdict)
    test.get(2)
    print(test.keys)
    print(test.sdict)
    test.put(1, 1)
    print(test.keys)
    print(test.sdict)
    test.put(4, 1)
    print(test.keys)
    print(test.sdict)
    test.get(2)
    print(test.keys)
    print(test.sdict)"""