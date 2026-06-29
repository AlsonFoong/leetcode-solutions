# Time: O(n^2) - Outer O(n) loop contains O(n) inner two-pointer loop
# Space: O(n) - Storing a results array with up to n elements
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Crucial for Two Sum II and duplicate handling
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Layer 1: Skip duplicate starting values
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 2: Set up Two Sum II pointers on the remaining subarray
            left = i + 1
            right = n - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Layer 2: Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move inward to keep searching the rest of the window
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1   # Need a larger value
                else:
                    right -= 1  # Need a smaller value
                    
        return result
