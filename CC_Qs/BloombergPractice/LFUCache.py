# https://leetcode.com/problems/lfu-cache/
import heapq
# use minheap to keep track

class LFUCache:
    def __init__(self, capacity: int):
        self.keys = list()
        self.sdict = dict()
        if capacity > 0:
            self.cap = capacity
        else:
            raise Exception("Invalid Capacity")

    def get(self, key: int) -> int:
        if key in self.sdict:
            self.sdict[key][2] += 1
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
            self.sdict[key][0] = value
            self.sdict[key][1] = len(self.keys) - 1
            self.sdict[key][2] += 1
        else:
            if len(self.keys) == self.cap:
                self.sdict.pop(self.keys[0])
                self.keys.pop(0)

            self.keys.append(key)
            self.sdict.setdefault(key, (value, len(self.keys)-1), 1)


class LFUCache2():
    def __init__(self, capacity: int):
        self.capacity = capacity
        # print(self.capacity)
        self.m = defaultdict(list)
        self.q = []

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        self.m[key][1] += 1
        indice = self.q.index(key)
        self.q.pop(indice)
        self.q.append(key)
        return self.m[key][0]

    def put(self, key: int, value: int) -> None:
        heap = []
        if key in self.m:
            self.m[key][0] = value
            self.m[key][1] += 1
            indice = self.q.index(key)
            self.q.pop(indice)
            self.q.append(key)
        else:
            if not self.m and len(self.q) == self.capacity:
                return
            if len(self.q) < self.capacity:
                self.m[key] = [value, 1]
                self.q.append(key)
            else:
                for i, j in self.m.items():
                    heapq.heappush(heap, (j[1], i))  # frequncey, value
                lowestFrequnceyPair = heapq.heappop(heap)
                temp = -1
                templowestFrePairs = [lowestFrequnceyPair]
                while heap:
                    temp = heap[0][0]
                    if temp == lowestFrequnceyPair[0]:
                        templowestFrePairs.append(heapq.heappop(heap))
                    else:
                        break
                removeindex = float('inf')
                # print(self.m, self.q, templowestFrePairs)
                for x, y in templowestFrePairs:
                    removeindex = min(removeindex, self.q.index(y))
                keydel = self.q.pop(removeindex)
                del self.m[keydel]

                self.m[key] = [value, 1]
                self.q.append(key)







if __name__ == '__main__':
    test = LFUCache(2)
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

