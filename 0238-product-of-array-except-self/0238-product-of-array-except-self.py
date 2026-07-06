class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n

        p = 1
        for i in range(n):
            res[i] = p
            p *= nums[i]

        s = 1
        for i in range(n - 1, -1, -1):
            res[i] *= s
            s *= nums[i]

        return res