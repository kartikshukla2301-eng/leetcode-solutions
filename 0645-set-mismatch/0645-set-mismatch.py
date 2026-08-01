class Solution:
    def findErrorNums(self, nums):
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        expected_sq = n * (n + 1) * (2 * n + 1) // 6

        actual_sum = sum(nums)
        actual_sq = sum(x * x for x in nums)

        diff = actual_sum - expected_sum
        sq_diff = actual_sq - expected_sq

        sum_dm = sq_diff // diff

        duplicate = (diff + sum_dm) // 2
        missing = duplicate - diff

        return [duplicate, missing]