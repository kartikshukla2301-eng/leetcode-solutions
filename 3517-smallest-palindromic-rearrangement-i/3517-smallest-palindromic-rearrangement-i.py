from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)

        first_half = []
        middle = ""

        for ch in map(chr, range(ord('a'), ord('z') + 1)):
            first_half.append(ch * (cnt[ch] // 2))
            if cnt[ch] % 2 == 1:
                middle = ch

        first = "".join(first_half)
        return first + middle + first[::-1]