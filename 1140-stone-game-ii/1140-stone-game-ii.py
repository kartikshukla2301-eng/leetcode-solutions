class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i, m):
            if i >= n:
                return 0

            # Can take all remaining piles
            if 2 * m >= n - i:
                return suffix[i]

            if (i, m) in dp:
                return dp[(i, m)]

            best = 0

            for x in range(1, 2 * m + 1):
                # Current player gets x piles
                # Remaining stones are for opponent
                opponent = solve(i + x, max(m, x))

                current = suffix[i] - opponent
                best = max(best, current)

            dp[(i, m)] = best
            return best

        return solve(0, 1)