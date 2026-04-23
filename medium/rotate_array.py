# Time: O(n) - Single traversal of list
# Space: O(n) - List created to store values
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # Missing this line that handles k > length
        shifted = []
        i = 0
        while i < (len(nums) - k):
            shifted.append(nums[i])
            i += 1
        nums.extend(shifted)
        del nums[:len(shifted)]

# Alternative - Triple Reversal
# Time: O(n) - Touching each element twice at most (one full reversal, one partial reversal)
# Space: O(1) - No other data structures, all swaps within nums
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n # Handle cases where k > n
        
        # Helper function to reverse a portion of the list
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # 1. Reverse the entire array
        reverse(0, n - 1)
        # 2. Reverse the first k elements
        reverse(0, k - 1)
        # 3. Reverse the rest
        reverse(k, n - 1)
