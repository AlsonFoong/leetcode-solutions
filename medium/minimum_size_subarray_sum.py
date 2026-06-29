# Time: O(n) - The inner while loop is a trap, as large contractions mean that many subsequent iterations won't move the left pointer, so the algorithm only visits every element twice
# Space: O(1) - Processes input in-place, no auxiliary data structures
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        count = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                count = min(count, right - left + 1)
                total -= nums[left]
                left += 1
        return count if count != float('inf') else 0
