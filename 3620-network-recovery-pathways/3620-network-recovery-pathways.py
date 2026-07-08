from collections import deque

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        g = [[] for _ in range(n)]
        indeg = [0] * n
        vals = []

        for u, v, w in edges:
            g[u].append((v, w))
            indeg[v] += 1
            vals.append(w)

        vals = sorted(set(vals))

        def check(limit):
            dist = [float('inf')] * n
            dist[0] = 0

            deg = indeg[:]
            q = deque(i for i in range(n) if deg[i] == 0)

            while q:
                u = q.popleft()

                if u != 0 and u != n - 1 and not online[u]:
                    for v, _ in g[u]:
                        deg[v] -= 1
                        if deg[v] == 0:
                            q.append(v)
                    continue

                if dist[u] != float('inf'):
                    for v, w in g[u]:
                        if w >= limit and dist[u] + w < dist[v]:
                            dist[v] = dist[u] + w

                        deg[v] -= 1
                        if deg[v] == 0:
                            q.append(v)
                else:
                    for v, _ in g[u]:
                        deg[v] -= 1
                        if deg[v] == 0:
                            q.append(v)

            return dist[-1] <= k

        lo, hi = 0, len(vals) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(vals[mid]):
                ans = vals[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans