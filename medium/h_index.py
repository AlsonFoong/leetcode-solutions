# Time: O(n log n) - Python sorting worst-case scenario
# Space: O(1) - Only declaration of variables
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, cite in enumerate(citations):
            # i + 1 represents the number of papers we are currently considering
            # If the current paper has at least i + 1 citations, then h could be i + 1
            if cite >= i + 1:
                h = i + 1
            else:
                # Since the list is sorted, if this paper doesn't qualify,
                # no subsequent paper will either.
                break
        return h
