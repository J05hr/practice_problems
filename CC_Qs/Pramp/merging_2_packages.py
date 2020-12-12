

class Solution:

    def get_indices_of_item_wights(self, arr, limit):
        d = dict()
        for idx, item in enumerate(arr, 0):
            if item not in d:
                d.setdefault(item, [idx])
            else:
                d[item].append(idx)

        for idx, item in enumerate(arr):
            trgt = limit - item
            if trgt in d:
                tia = d[trgt]
                for ti in tia:
                    if idx != ti:
                        return [ti, idx]
        return []

    def get_indices_of_item_wights2(self, arr, limit):
        d = dict()
        for idx, item in enumerate(arr):
            trgt = limit - item
            if trgt in d:
                tia = d[trgt]
                for ti in reversed(tia):
                    if idx != ti:
                        return [idx, ti]
            if item not in d:
                d.setdefault(item, [idx])
            else:
                d[item].append(idx)
        return []


if __name__ == '__main__':
    tester = Solution()
    # ans = tester.get_indices_of_item_wights([4, 6, 10, 15, 16], 21)
    ans = tester.get_indices_of_item_wights2([4, 4, 1], 5)
    print(ans)
