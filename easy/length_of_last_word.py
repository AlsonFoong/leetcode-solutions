# Time: O(1) - Deteriorates to O(n) in worst-case scenario
# Space: O(1) - No data structures used, only variables
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
            elif length > 0:
                break
        
        return length
