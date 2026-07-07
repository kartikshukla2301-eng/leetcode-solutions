class Solution(object):
    def sumAndMultiply(self, n):
        s = 0
        x = '0'
        for i in str(n):
            if i != '0':
                s += int(i)
                x += i
        return int(x) * s