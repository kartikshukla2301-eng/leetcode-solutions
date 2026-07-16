class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        from math import gcd
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefix_gcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefix_gcd.append(gcd(num, mx))

        prefix_gcd.sort()

        ans = 0
        left, right = 0, len(prefix_gcd) - 1

        while left < right:
            ans += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return ans