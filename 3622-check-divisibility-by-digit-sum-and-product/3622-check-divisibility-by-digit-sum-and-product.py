class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        s, p = 0, 1

        while n:
            n, d = divmod(n, 10)
            s += d
            p *= d

        return original % (s + p) == 0