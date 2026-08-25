from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Convert to prefix sums in-place
        for i in range(1, len(stones)):
            stones[i] += stones[i - 1]

        # Base case: eventually all stones are merged
        best = stones[-1]

        # Work backwards
        for i in range(len(stones) - 2, 0, -1):
            best = max(best, stones[i] - best)

        return best