class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low, high=0,0
        for i in range(len(s)):
            if s[i]=="(":
                low+=1
                high+=1
            elif s[i]==")":
                low= max(0,low-1)
                high-=1
            elif s[i]=="*":
                low=max(0,low-1)
                high+=1
            if high<0:
                return False
        return low==0
        

