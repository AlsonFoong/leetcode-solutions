# Tiem: O(n) - Will compare every string in a worst-case scenario
# Space: O(1) - Note that Python string slicing allocates a new string object, but len(base) never exceeds len(strs[0]), so it is
#               considered auxiliary memory overhead relative to the size of the input array.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]

        for i in range(1, len(strs)):
            string = strs[i]
            j = 0
            while (j < len(base) and j < len(string) and base[j] == string[j]):
                j += 1
            base = base[:j]
            if base == '':
                return ''

        return base
