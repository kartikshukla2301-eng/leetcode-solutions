class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pro=1
        zero=0
        for i in nums:
            if i!=0:
                pro*=i
            else:
                zero+=1
        if zero==0:
            res=[pro/i for i in nums]
        elif zero>1:
            res=[0 for i in nums]
        else:
            res=[0 if i!=0 else pro for i in nums]
        return res