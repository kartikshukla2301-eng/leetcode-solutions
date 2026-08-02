from typing import List
from bisect import bisect_left

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countRatioSubarrays(self, nums: List[int], a: int, b: int) -> int:
        n = len(nums)

        prefixes = []
        odd = even = 0

        # prefix 0
        prefixes.append((0, 0))

        for x in nums:
            if x & 1:
                odd += 1
            else:
                even += 1
            prefixes.append((odd, b * even - a * odd))

        vals = sorted({v for _, v in prefixes})
        m = len(vals)

        bit = BIT(m)

        ans = 0
        pending = []
        current_odd = 0

        for odd, val in prefixes:
            if odd != current_odd:
                for v in pending:
                    idx = bisect_left(vals, v) + 1
                    bit.add(idx, 1)
                pending = []
                current_odd = odd

            idx = bisect_left(vals, val) + 1

            # count previous prefixes having value >= current value
            ans += bit.sum(m) - bit.sum(idx - 1)

            pending.append(val)

        return ans