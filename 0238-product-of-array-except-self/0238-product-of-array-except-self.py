class Solution:
    def productExceptSelf(self, nums):
        prod = 1
        zero = nums.count(0)

        if zero > 1:
            return [0] * len(nums)

        for x in nums:
            if x != 0:
                prod *= x

        ans = []
        for x in nums:
            if zero:
                ans.append(prod if x == 0 else 0)
            else:
                ans.append(prod // x)

        return ans