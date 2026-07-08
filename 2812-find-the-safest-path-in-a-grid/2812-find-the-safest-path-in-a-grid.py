from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)

        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dist[i][j] = 0
                    q.append((i, j))

        dirs = (1, 0, -1, 0, 1)

        while q:
            x, y = q.popleft()
            d = dist[x][y] + 1
            for k in range(4):
                nx = x + dirs[k]
                ny = y + dirs[k + 1]
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = d
                    q.append((nx, ny))

        def check(limit):
            if dist[0][0] < limit:
                return False

            q = deque([(0, 0)])
            vis = [[False] * n for _ in range(n)]
            vis[0][0] = True

            while q:
                x, y = q.popleft()
                if x == n - 1 and y == n - 1:
                    return True

                for k in range(4):
                    nx = x + dirs[k]
                    ny = y + dirs[k + 1]

                    if (
                        0 <= nx < n
                        and 0 <= ny < n
                        and not vis[nx][ny]
                        and dist[nx][ny] >= limit
                    ):
                        vis[nx][ny] = True
                        q.append((nx, ny))

            return False

        lo, hi = 0, n * 2

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo