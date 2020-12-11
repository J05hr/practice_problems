

class Solution:

    def maxProfit(self, prices):
        maxP = 0
        min = float("inf")

        # traverse the list to find the local max idx
        for price in range(len(prices)):
            if price < min:
                min = price

            profit = price - min

            if profit > maxP:
                maxP = profit

        return maxP


if __name__ == '__main__':
    tester = Solution()
    ans = tester.maxProfit([9,1,10,5,6,3,20,1,1,1,90,2,-1, 50])
    print(ans)
