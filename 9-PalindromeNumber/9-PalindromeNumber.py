# Last updated: 3/12/2026, 4:59:27 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x<0 or (x%10==0 and x!=0):
4            return False
5        
6        og= x
7        reversed_num=0
8
9        while x>0:
10            last_digit = x%10
11            reversed_num = (reversed_num*10)+last_digit
12            x= x//10
13        return og==reversed_num
14        
15