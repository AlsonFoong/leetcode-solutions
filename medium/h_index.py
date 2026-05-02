# Time: O(n log n) - Python sorting worst-case scenario
# Space: O(1) - Only declaration of variables
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            if i + 1 <= citations[i]:
                h = i + 1
            else:
                break
        return h

# Alternative: Bucket Sort
# Time: O(n) - Single traversal of list
# Space: O(1) - Only declaration of variables
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)
        # Fill buckets: anything over n citations goes into the last bucket
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
        # Walk backwards through buckets to find the H-index
        total_papers = 0
        for h in range(n, -1, -1):
            total_papers += buckets[h]
            if total_papers >= h:
                return h
        return 0
