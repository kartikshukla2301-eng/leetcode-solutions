class Solution:
    def findMissingElements(self, nums):
        mn, mx = min(nums), max(nums)
        s = set(nums)
        return [i for i in range(mn, mx + 1) if i not in s]