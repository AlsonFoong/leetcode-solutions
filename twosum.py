class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []
# Due to the nature of complements, there is no need to worry about "missing" complements further into the array.
# When the algorithm eventually passes over the "missed" answer, it will match up with its complement we previously saved to the hashmap.
