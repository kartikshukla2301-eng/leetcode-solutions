class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        mp = {}

        for i, num in enumerate(sorted_nums):
            if num not in mp:
                mp[num] = i

        return [mp[num] for num in nums]