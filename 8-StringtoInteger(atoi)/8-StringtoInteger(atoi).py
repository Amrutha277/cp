class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()

        if not s:
            return 0

        sign = 1

        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign= 1
            s = s[1:]
        
        result = 0
        for char in s:
            if char.isdigit():
                result = result*10+ int(char)
            else:
                break
        
        result= sign*result

        min_lim= -2**31
        max_lim= 2**31-1

        if result<min_lim:
            result= min_lim
        elif result>max_lim:
            result = max_lim

        return result


         
    