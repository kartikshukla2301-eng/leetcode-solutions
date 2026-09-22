from typing import List


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        # tree[node] = [product % k, counts]
        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            lp, lc = left
            rp, rc = right

            # Product of entire combined segment
            prod = (lp * rp) % k

            # Prefixes completely inside left
            cnt = lc[:]

            # Prefixes that cross from left into right
            for r in range(k):
                nr = (lp * r) % k
                cnt[nr] += rc[r]

            return [prod, cnt]

        def build(node, l, r):
            if l == r:
                v = nums[l] % k

                tree[node][0] = v
                tree[node][1][v] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, pos, value):
            if l == r:
                value %= k

                tree[node][0] = value
                tree[node][1] = [0] * k
                tree[node][1][value] = 1
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2, l, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, r, pos, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            # Completely inside range
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            # Entirely left
            if qr <= mid:
                return query(
                    node * 2,
                    l,
                    mid,
                    ql,
                    qr
                )

            # Entirely right
            if ql > mid:
                return query(
                    node * 2 + 1,
                    mid + 1,
                    r,
                    ql,
                    qr
                )

            # Crosses midpoint
            left = query(
                node * 2,
                l,
                mid,
                ql,
                qr
            )

            right = query(
                node * 2 + 1,
                mid + 1,
                r,
                ql,
                qr
            )

            return merge(left, right)

        # Build
        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            # Persistent point update
            update(
                1,
                0,
                n - 1,
                index,
                value
            )

            # Query nums[start ... n-1]
            result = query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            ans.append(result[1][x])

        return ans