class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result=[]
        def pal_check(start, end, s):
            while start<=end:
                if s[start]!=s[end]:
                    return False
                
                start+=1
                end -=1
            return True
            
        def helper(index, curr_set):
            if index== len(s):
                result.append(curr_set[:])
                return
            
            for i in range(index,len(s)):
                if pal_check(index, i, s):
                    curr_set.append(s[index:i+1])
                    helper(i+1, curr_set)
                    curr_set.pop()
        helper(0,[])
        return result
            