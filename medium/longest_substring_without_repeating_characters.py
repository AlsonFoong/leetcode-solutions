# Time: O(n) - Single traversal of string; each character added and removed at most once
# Space: O(k) - Up to all 26 letters stored (k is bounded by the size of the alphabet)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        length = 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            length = max(length, right - left + 1)
        return length
# 1. It is a good idea to remember the template of a variable-sized sliding window.
#    Straying from it likely indicates that the code should be refactored.
