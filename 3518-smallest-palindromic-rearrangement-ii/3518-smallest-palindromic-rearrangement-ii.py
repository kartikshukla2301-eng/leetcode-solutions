from collections import Counter
from math import comb

class Solution:
    LIMIT = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""

        for ch in sorted(freq):
            if freq[ch] % 2:
                mid = ch
            half[ord(ch) - 97] = freq[ch] // 2

        if self.countWays(half) < k:
            return ""

        left = []

        while sum(half):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = self.countWays(half)

                if ways >= k:
                    left.append(chr(i + 97))
                    break

                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def countWays(self, cnt):
        total = sum(cnt)
        ans = 1
        rem = total

        for c in cnt:
            if c:
                ans *= comb(rem, c)
                if ans > self.LIMIT:
                    return self.LIMIT
                rem -= c

        return min(ans, self.LIMIT)