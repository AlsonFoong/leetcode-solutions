# Time: O(n) - Single traversal of array
# Space: O(1) - Variables only store integers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        front = 0
        back = len(height) - 1
        volume = 0
        while front < back:
            min_height = min(height[front], height[back])
            distance = back - front
            volume = max(volume, min_height * distance)
            if height[front] < height[back]:
                front += 1
            else:
                back -= 1
        return volume
# 1. The breakthrough comes in the form of realizing that a lookahead isn't necessary.
#    Do not try to pick the next tallest height, just move on from the current lowest height.
