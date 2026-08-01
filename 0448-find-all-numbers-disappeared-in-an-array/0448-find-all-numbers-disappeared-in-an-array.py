class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans