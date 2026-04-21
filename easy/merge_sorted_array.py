# Time: O(N log N) - Python sorting algorithm complexity, where N is the total number of elements
# Space: O(N) - Python sorting algorithm complexity, where N is the total number of elements
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
