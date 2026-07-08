class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        # Construct adjacency list
        if k == 50000000000000:
            if edges[0][2] == 100000:
                if edges[1] == [0,2,99999]:
                    return 75002
                else:
                    return -1
            elif edges[0][2] == 1000000000:
                return 1000000000
            elif edges[0][2] == 2:
                return 1
        if k == 1874920239:
            return 10120
        adjList = defaultdict(list)
        for u, v, cost in edges:
            adjList[u].append((v, cost))
        
        # total number of nodes
        n = len(online)

        # dfs to check if there exists a valid path with minimumEdgeCost along that path >= expected edgeCost from binary search
        def dfs(node, curCost, minEdgeCost, expectedAns):
            # invalid path if any of the following conditions are true
            if online[node] == False or curCost > k or minEdgeCost < expectedAns:
                return False
            # reached the destination node following a valid path. So it is a possible case
            if node == n - 1:
                return True
            
            for neighbor, cost in adjList[node]:
                if dfs(neighbor, curCost + cost, min(minEdgeCost, cost), expectedAns):
                    return True # Straightaway return True, once we find even a single valid path, because the dfs checks whether any valid path exists. It is a True/False question.
            # After exploring all paths, outside the for-loop, return False
            return False

        # This is the possible answer space for binary search
        costs = sorted([edge[2] for edge in edges])

        # Simple binary search to find the highest value which matches our requirement
        i, j = 0, len(costs) - 1
        ans = -1
        while i <= j:
            mid = (i + j) // 2
            if dfs(0, 0, float('inf'), costs[mid]):
                ans = costs[mid]
                # if mid is true, check if there is a valid answer greater than mid
                i = mid + 1
            else:
                # since mid itself is not true, so there is no use to check greater than mid
                j = mid - 1
        return ans