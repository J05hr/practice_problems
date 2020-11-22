# https://leetcode.com/problems/two-city-scheduling/description/

class Solution:
    def twoCitySchedCost(self, costs):
        # define a final result
        self.minCost = 0
        # keep count for city a
        self.aCount = 0
        # keep count for city b
        self.bCount = 0

        # define a sorting method, use difference
        def getDif(cost):
            return abs(cost[1] - cost[0])

        # define a method for getting minItem when balanced
        def recMin(cost):
            if cost[0] < cost[1]:
                self.aCount += 1
                self.minCost += cost[0]
            else:
                self.bCount += 1
                self.minCost += cost[1]

        # sort the cost list by cost difference
        costs.sort(key=getDif, reverse=True)

        # loop through the costs array
        for costIdx in range(len(costs)):
            cost = costs[costIdx]
            # add greedily until we have to balance then just take the one needed to stay balanced
            if self.aCount == len(costs)/2:
                self.minCost += cost[1]
                self.bCount += 1
            elif self.bCount == len(costs)/2:
                self.minCost += cost[0]
                self.aCount += 1
            else:
                recMin(cost)

        return self.minCost


if __name__ == '__main__':
    tester = Solution()
    ans = tester.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
    # ans2 = tester.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
    print(ans)
