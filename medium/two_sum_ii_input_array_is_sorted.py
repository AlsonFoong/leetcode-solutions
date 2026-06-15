# Time: O(n) - Up to every element passed during execution
# Space: O(1) - Only primitive values initialized
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            if curr_sum > target:
                right -= 1
            else:
                left += 1
# 1. The secret here is to understand that moving the left pointer up will increase the current sum,
#    while moving the right pointer back will decrease the current sum.
