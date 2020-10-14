

from typing import List

class Solution:
    prices2 = [7, 1, 5, 3, 6, 4]
    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    def maxProfit(self, prices: List[int]) -> int:

        maxy = 0
        lastmax = 0

        # traverse the list to find the local max idx
        for idx in range(len(prices)):
            # end is the max if we reach it or we are at local max
            if (idx == len(prices) - 1) or (prices[idx] > prices[idx + 1]):
                # traverse the list from last max to new max and find a min
                damin = prices[lastmax]
                for idx2 in range(lastmax, idx):
                    if prices[idx2] < damin:
                        damin = prices[idx2]
                lastmax = idx
                # calc the profit
                if damin < prices[idx]:
                    maxy += prices[idx] - damin

        return maxy


memes = Solution()

print(memes.maxProfit(memes.prices2))
