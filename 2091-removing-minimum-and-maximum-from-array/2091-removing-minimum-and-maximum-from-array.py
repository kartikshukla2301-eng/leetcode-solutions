class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        left = min(mn, mx)
        right = max(mn, mx)

        # 1. Remove both from the front
        front = right + 1

        # 2. Remove both from the back
        back = n - left

        # 3. Remove left one from front, right one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)