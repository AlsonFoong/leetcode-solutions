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

# Alternative: Optimal mathematical approach
# Time: O(n) - Single traversal of string characters
# Space: O(1)* - Constant *auxiliary memory overhead because only string and primitives loop variables are stored
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = []
        n = len(s)
        cycle_jump = 2 * numRows - 2

        for i in range(numRows):
            j = i

            while j < n: # Making sure it's not out of range
                result.append(s[j]) # Adds first variable on new row
                if i != 0 and i != numRows - 1:
                    diagonal_index = j + cycle_jump - (2 * i) # Hard part involves deriving formula
                    if diagonal_index < n: # Making sure it's not out of range
                        result.append(s[diagonal_index])
                j += cycle_jump # Jumping to same place in next cycle
            
        return ''.join(result)
# 1. Using `try...except` should be a sign to add conditional logic such as `while j < n` instead.
