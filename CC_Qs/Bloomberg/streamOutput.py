# https://leetcode.com/discuss/interview-question/314733/Bloomberg-or-Output-data-from-a-stream-in-order



# use minheap

# https://www.geeksforgeeks.org/min-heap-in-java/

"""
    getMin(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).
    extractMin(): Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Log n) as this operation needs to maintain the heap property (by calling heapify()) after removing root.
    insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree. If new key is larger than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
"""



import heapq



class Solution:
    def func(self, list):
        heapq.heapify(list)
        while len(list) > 0:
            print(heapq.heappop(list))


if __name__ == '__main__':
    tester = Solution()
    ans = tester.func(list())
    print(ans)