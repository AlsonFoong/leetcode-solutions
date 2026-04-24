# Time: O(n) - Single traversal of list
# Space: O(1) - Only declaration of variables
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
# 1. Imagine trying to get to a leaf by guessing which branch to climb up. Instead, start from the leaf (the end) and navigate back to the root. That is the logic at play here.
