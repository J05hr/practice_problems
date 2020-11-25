import math

def purchasingSupplies(budget, cost, tcontainers):

    boughtContainers = math.floor(budget/cost)
    tradeContainers = math.floor(boughtContainers/tcontainers)
    maxcontainers = boughtContainers + tradeContainers
    return maxcontainers


if __name__ == '__main__':
    print(purchasingSupplies(7, 2, 3))