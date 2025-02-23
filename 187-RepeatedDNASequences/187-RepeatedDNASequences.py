class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n <10:
            return []
        left = 0
        count=0
        right = left+10
        result= set()
        seen= set()
        # result=[]
        while right<=n:
            seq = s[left:right]
            if seq in seen:
                result.add(seq)
            else:
                seen.add(seq)
            left+=1
            right+=1
                
        return list(result)