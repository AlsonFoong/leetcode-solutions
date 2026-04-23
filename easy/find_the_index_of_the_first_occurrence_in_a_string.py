# Time: O(N) - Traversal of lists, where N is the total number of elements (m + n)
# Space: O(1) - Only declaration of variables
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
