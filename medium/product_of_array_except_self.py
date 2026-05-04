# Time - O(n): Two traversals of the list
# Space - O(1): Output array does not count towards space complexity analysis
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        front = 1
        for i in range(n):
            output[i] *= front
            front *= nums[i]
        back = 1
        for j in range(n - 1, -1, -1):
            output[j] *= back
            back *= nums[j]
        return output
# 1. Input: [1, 2, 3, 4]
#            Indexes of numbers to be multiplied with nums[i]:
#    Front:  .  0  0  0
#                  1  1
#                     2
#     Back:  3  3  3
#            2  2
#            1
# 2. As seen in the visualization above, for any given nums[i], it is multiplied by every other number except itself over the course of 2 different iterations, that being "front" and "back".
#    For example, nums[1] is multiplied by nums[0] during the "front" iteration. then it is multiplied by nums[3] and nums[2] during the "back" iteration.
