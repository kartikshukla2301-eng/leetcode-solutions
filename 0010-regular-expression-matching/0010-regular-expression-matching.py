from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(None)
        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            if j + 1 < len(p) and p[j + 1] == '*':
                return (
                    dfs(i, j + 2) or
                    (first_match and dfs(i + 1, j))
                )

            return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)