class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        # Sort the nums and convert the indices
        idx = sorted(range(n), key=nums.__getitem__)
        mapping = {j:i for i,j in enumerate(idx)}
        
        # Find the furthest step to the left for each node
        ptr, prv = 0, []
        for j in idx:
            while nums[j] - nums[idx[ptr]] > maxDiff:
                ptr += 1
            prv.append(ptr)
        
        # Build the trees with the reversing pointers from the previous step, and collect the roots
        rts, conn = [], [[] for _ in range(n)]
        for i,p in enumerate(prv):
            if i == p:
                rts.append(i)
            else:
                conn[p].append(i)
            
        # DFS, collect the root, level and post-order number of each node
        def dfs(node: int):
            parent = prv[node]
            root[node] = root[parent]
            level[node] = level[parent] + 1
            order[node] = order[parent]
            for nxt in conn[node]:
                dfs(nxt)
            order[parent] = order[node] + 1
            
        root, level, order = list(range(n)), [0] * n, [0] * n
        for i in rts:
            dfs(i)
                
        # Online, O(1) per query
        ans = []
        for u,v in queries:
            u,v = mapping[u], mapping[v]
            if root[u] != root[v]:
                # Not in the same tree
                ans.append(-1)
            else:
                if u < v:
                    u,v = v,u
                # Get the level difference as their distance
                ans.append(level[u] - level[v] + (order[u] > order[v]))
                
        return ans