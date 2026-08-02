from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prevTime = 0

        for log in logs:
            fid, status, time = log.split(":")
            fid = int(fid)
            time = int(time)

            if status == "start":
                if stack:
                    ans[stack[-1]] += time - prevTime
                stack.append(fid)
                prevTime = time
            else:
                ans[stack.pop()] += time - prevTime + 1
                prevTime = time + 1

        return ans