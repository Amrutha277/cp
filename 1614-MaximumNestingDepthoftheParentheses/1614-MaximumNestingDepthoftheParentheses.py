# Last updated: 3/11/2026, 3:41:04 PM
1class Solution:
2    def maxDepth(self, s: str) -> int:
3        max_d= 0
4        cur_d=0
5        for char in s:
6            if char == '(':
7                cur_d +=1
8                if cur_d > max_d:
9                    max_d = cur_d
10            elif char == ')':
11                cur_d -=1
12        return max_d