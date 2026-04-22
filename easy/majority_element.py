# Time: O(n) - Single traversal of list, dictionary lookups and insertions are O(1) on average
# Space: O(n) - Every element stored in worst-case scenario
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] > len(nums) // 2:
                return num

# Alternative - Boyer-Moore Voting Algorithm:
# Time: O(n) - Single traversal of list
# Space: O(1) - Only declaration of variables
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
# 1. This algorithm essentially makes numbers duel each other until only one winner remains.
#    The candidate gets stronger when it encounters more of its own, and gets weaker when it eliminates other numbers.
