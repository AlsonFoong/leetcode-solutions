# Time: O(n) - Where n is the length of t
# Space: O(1) - Only primitive integers stored
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps, pt = 0, 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        return ps == len(s)

# Alternative: Binary search inverted index
# Time: O(log n) - Search space cut in half for every iteration
# Space (Iterative): O(1) - Only primtive integers after hashmap creation
# Space (Recursive): O(log n) - Every recursive call pushes a stack frame, and the maximum depth of the call stack matches the maximum number of steps  
import bisect
from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pre-process t
        char_to_indices = defaultdict(list)
        for index, char in enumerate(t):
            char_to_indices[char].append(index)
            
        current_index = -1
        for char in s:
            if char not in char_to_indices:
                return False
                
            indices = char_to_indices[char]
            # bisect_right finds where to place current_index to the right of matches
            idx_pos = bisect.bisect_right(indices, current_index)
            
            # If the insertion position is at the end of the array, no larger index exists
            if idx_pos == len(indices):
                return False
                
            current_index = indices[idx_pos]
            
        return True
