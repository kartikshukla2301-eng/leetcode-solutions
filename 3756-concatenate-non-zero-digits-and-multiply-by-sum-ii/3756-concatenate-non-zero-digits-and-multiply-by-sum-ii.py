from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        pref_sum = [0] * (n + 1)
        pref_cnt = [0] * (n + 1)
        pref_val = [0] * (n + 1)

        for i in range(n):
            d = ord(s[i]) - ord('0')
            pref_sum[i + 1] = pref_sum[i] + d

            if d:
                pref_cnt[i + 1] = pref_cnt[i] + 1
                pref_val[i + 1] = (pref_val[i] * 10 + d) % MOD
            else:
                pref_cnt[i + 1] = pref_cnt[i]
                pref_val[i + 1] = pref_val[i]

        pow10 = [1] * (pref_cnt[-1] + 1)
        for i in range(1, len(pow10)):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        ans = []

        for l, r in queries:
            cnt = pref_cnt[r + 1] - pref_cnt[l]
            sm = pref_sum[r + 1] - pref_sum[l]

            if cnt == 0:
                ans.append(0)
                continue

            x = (pref_val[r + 1] - pref_val[l] * pow10[cnt]) % MOD
            ans.append((x * sm) % MOD)

        return ans