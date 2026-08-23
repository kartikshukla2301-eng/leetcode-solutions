class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        left = right = ql = qr = 0

        for i, ch in enumerate(num):
            if ch == '?':
                if i < mid:
                    ql += 1
                else:
                    qr += 1
            elif i < mid:
                left += int(ch)
            else:
                right += int(ch)

        return (ql + qr) % 2 == 1 or left - right != 9 * (qr - ql) // 2