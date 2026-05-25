# Time: O(n) - Single traversal of string characters
# Space: O(n) - Linear storage overhead due to rows variable storing all characters
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return ''.join(rows)
# 1. It helps to assess problems from a different perspective. A purely mathematical approach may work, but it
#    may not be easily conceived or debugged. Simulating the traversal itself using buckets is a standard approach.
