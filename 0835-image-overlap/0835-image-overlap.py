from collections import Counter

class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        ones1 = []
        ones2 = []

        # Store coordinates of all 1s
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones1.append((r, c))

                if img2[r][c] == 1:
                    ones2.append((r, c))

        # Count translation vectors
        shifts = Counter()

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shifts[(r2 - r1, c2 - c1)] += 1

        return max(shifts.values(), default=0)