# Last updated: 7/9/2025, 7:58:12 PM
class Solution:
    def myAtoi(self, s: str) -> int:
        s= s.lstrip()
        if not s:
            return 0
        sign=1
        if s[0] =='-':
            sign= -1
            s= s[1:]
        elif s[0] =='+':
            s= s[1:]
        s= s.lstrip("0")
        print(s)
        res= []

        for char in s:
            if char.isdigit():
                res.append(char)
            else:
                break
        print(res)
        if not res:
            return 0
        num=0
        for i in range(len(res)):
            num= num*10 + int(res[i])
            print(num)
        
        if sign == -1:
            num= -1* num

        
        if num < -2**31:
            num= -2**31
        elif num> 2**31-1:
            num= 2**31-1

        return num