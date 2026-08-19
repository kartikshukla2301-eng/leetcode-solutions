from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] = rows.get(row, 0) | (1 << seat)

        # Every untouched row can fit 2 families
        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = all((mask & (1 << seat)) == 0 for seat in (2, 3, 4, 5))
            right = all((mask & (1 << seat)) == 0 for seat in (6, 7, 8, 9))
            middle = all((mask & (1 << seat)) == 0 for seat in (4, 5, 6, 7))

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans