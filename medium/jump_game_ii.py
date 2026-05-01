# Time: O(n^2) - Repeatedly looking through entire list in worst case scenario
# Space: O(1) - Only declaration of variables
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        goal = len(nums) - 1
        # Keep jumping until we reach the start of the array
        while goal > 0:
            # Look for the leftmost index that can reach the current goal
            for i in range(goal):
                # If index i can reach the goal or beyond...
                if i + nums[i] >= goal:
                    goal = i    # Move the goal to this new "earliest" point
                    jumps += 1  # We've committed to one jump to reach the old goal
                    break       # Stop searching the for-loop and start over from the new goal
        return jumps

# Alternative:
# Time: O(n) - Single traversal of list
# Space: O(1) - Only declaration of variables
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        furthest_reach = 0
        # We don't need to jump from the last element (referring to other solution)
        for i in range(len(nums) - 1):
            # Update how far we could possibly get
            furthest_reach = max(furthest_reach, i + nums[i])
            # If we've reached the end of our current jump's range...
            if i == current_end:
                jumps += 1            # We MUST jump
                current_end = furthest_reach # Our new window extends to the best reach we found
                # If we can already hit the goal, we can stop early
                if current_end >= len(nums) - 1:
                    break
        return jumps
