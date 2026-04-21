# Time: O(n) - Single traversal of list, and O(1) on average for hashmap lookup
# Space: O(n) - Almost every element stored in hashmap in worst-case scenario
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []
# 1. Due to the nature of complements, there is no need to worry about "missing" complements further into the array.
#    When the algorithm eventually passes over the "missed" answer, it will match up with its complement we previously saved to the hashmap.
# 2. Checking for the complement before adding the number to the hashmap naturally prevents the algorithm from using the same number twice.
