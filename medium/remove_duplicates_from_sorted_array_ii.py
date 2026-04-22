# Time: O(n) - Single traversal of list
# Space: O(1) - Two variable declarations
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if nums[k - 2] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k
# 1. It helps to see nums[k - 2] as a grandparent, a way to know where to position the k pointer (after the grandparent and parent) that keeps track of what number needs changing.
#    When nums[k - 2] == nums[i], it means we've reached a 3rd copy of the same number, and can thus stop incrementing k to keep the pointer right on the number that needs changing.
