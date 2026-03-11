# Last updated: 3/11/2026, 2:52:40 PM
1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1 or numRows >= len(s):
4            return s
5        rows = ["" for _ in range(numRows)]
6        current_row= 0
7        step = 1 
8
9        for char in s:
10            rows[current_row] +=char
11            if current_row == 0:
12                step =1
13            elif current_row== numRows-1:
14                step =-1
15            
16            current_row+=step
17        return "".join(rows)
18