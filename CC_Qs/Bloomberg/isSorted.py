# Given an array return whether the array is sorted or not (boolean).

class Solution:
    def isSorted(self, arr):

        if len(arr) < 2:
            return True

        Asc = False
        Dsc = False
        last = None

        for item in arr:
            if Asc:
                if last - item < 0:
                    return False
            elif Dsc:
                if last - item > 0:
                    return False
            else:
                if last is not None:
                    if last - item > 0:
                        Asc = True
                    elif last - item < 0:
                        Dsc = True
            last = item

        return True


if __name__ == '__main__':
    tester = Solution()
    ans = tester.func(None)
    print(ans)
