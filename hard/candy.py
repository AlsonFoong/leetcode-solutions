# Time: O(n) - Two traversals of the list
# Space: O(n) - Variable to store candies array
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        count = 0
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])
            count += candies[i - 1]
        return count + candies[n - 1]
# 1. The goal here is to traverse from the left to account for left-side neighbors, then traversing from the right to account for right-side neighbors.
