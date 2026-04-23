# Time: O(n) - Single traversal of list
# Space: O(1) - Only declaration of variables
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        purchase_price = prices[0]
        for p in prices[1:]:
            if purchase_price > p:
                purchase_price = p
            profit = max(profit, p - purchase_price)
        return profit
# 1. The intent here isn't to always know the best purchase price. It's to maximize profit. Even if the purchase price is changed later on, profit = max() ensures that the maximum profit is forver locked in.
