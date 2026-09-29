class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Valid parentheses string must have even length
        if (m + n - 1) % 2 != 0:
            return False

        # dp[i][j] = set of possible balances at (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Starting cell must be '('
        if grid[0][0] == ')':
            return False

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                for balance in range(m + n):
                    new_balance = balance

                    if i > 0 and balance in dp[i - 1][j]:
                        new_balance = balance + (1 if grid[i][j] == '(' else -1)

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

                    if j > 0 and balance in dp[i][j - 1]:
                        new_balance = balance + (1 if grid[i][j] == '(' else -1)

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]