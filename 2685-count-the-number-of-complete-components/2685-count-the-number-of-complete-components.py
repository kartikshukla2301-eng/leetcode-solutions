from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            vertices = 1
            degree_sum = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    v, d = dfs(nei)
                    vertices += v
                    degree_sum += d

            return vertices, degree_sum

        ans = 0

        for i in range(n):
            if not visited[i]:
                vertices, degree_sum = dfs(i)
                edges_count = degree_sum // 2

                if edges_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans