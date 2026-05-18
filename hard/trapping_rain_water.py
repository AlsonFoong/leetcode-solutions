# Time: O(n) - Forward and backward traversal of list
# Space: O(n) - Storage of list in variables
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        water = 0

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            water += water_level - height[i]
        
        return water
# 1. The idea here is to find the maximum height of the elevation map on a given element's left and right. This avoids the need for
#    complicated algorithms by simply focusing on the water contained by each column.
