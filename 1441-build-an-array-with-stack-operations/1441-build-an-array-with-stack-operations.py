from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        j = 0

        for num in range(1, n + 1):
            if j == len(target):
                break

            ans.append("Push")

            if num == target[j]:
                j += 1
            else:
                ans.append("Pop")

        return ans