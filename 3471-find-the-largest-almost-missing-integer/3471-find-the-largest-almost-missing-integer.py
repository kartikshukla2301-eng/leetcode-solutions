from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: k == 1
        # Each element forms its own subarray of size 1.
        # An integer is almost missing if it appears exactly once in the entire array.
        if k == 1:
            freq = Counter(nums)
            candidates = [num for num, count in freq.items() if count == 1]
            return max(candidates, default=-1)
            
        # Case 2: k == n
        # There is only 1 subarray of size n (the entire array).
        # Every unique element appears in this single subarray.
        if k == n:
            return max(nums)
            
        # Case 3: 1 < k < n
        # Interior elements (indices 1 to n-2) are covered by at least 2 windows.
        # Only the end elements (index 0 and index n-1) can appear in exactly 1 window,
        # provided they do not repeat anywhere else in the array.
        candidates = []
        if nums.count(nums[0]) == 1:
            candidates.append(nums[0])
        if nums.count(nums[-1]) == 1:
            candidates.append(nums[-1])
            
        return max(candidates, default=-1)