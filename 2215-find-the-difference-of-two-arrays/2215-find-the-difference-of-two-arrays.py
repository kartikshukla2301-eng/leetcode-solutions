class Solution:
    def findDifference(self, nums1, nums2):
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]