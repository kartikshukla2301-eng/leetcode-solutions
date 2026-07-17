from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        gcd_cnt = [0] * (mx + 1)

        # Count pairs having exact gcd = i
        for i in range(mx, 0, -1):
            cnt = 0
            for j in range(i, mx + 1, i):
                cnt += freq[j]
                gcd_cnt[i] -= gcd_cnt[j]
            gcd_cnt[i] += cnt * (cnt - 1) // 2

        # Prefix sums
        for i in range(2, mx + 1):
            gcd_cnt[i] += gcd_cnt[i - 1]

        ans = []
        for q in queries:
            ans.append(bisect_right(gcd_cnt, q))
        return ans