# Time: O(n) - Single traversal of list
# Space: O(1) - Only declaration of variables
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit
# 1. There is no need to find local minimums and maximums. A greedy algorithm that sells as soon as there is profit the next day works just as well.
