class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal= nums[-1]
        
        for i in range((len(nums)) -1,-1,-1):
            print(goal,"fdfd")
            if i+nums[i]>=goal:
                goal=i
                print(goal)
        return True if goal==0 else False
        

            

        


