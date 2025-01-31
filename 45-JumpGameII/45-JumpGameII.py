class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        goal=len(nums)-1
        l,r=0,0
        steps=0
        while r<goal:
            farthest=0
            for i in range(l, r+1):
                farthest= max(farthest, i+nums[i])
            l = r+1
            r = farthest
            steps+=1
        return steps

            
        return steps