# Last updated: 3/10/2026, 8:01:51 PM
1class Solution:
2    def maxValue(self, n: int, index: int, maxSum: int) -> int:
3        def side_sum(peak:int, count:int) -> int:
4            start = peak-1
5            if start>= count:
6                return (start + (start-count+1))*count//2
7            else:
8                decreasing_part = start*(start+1)//2
9                ones_part = count-start
10                return decreasing_part+ ones_part
11        
12        def can_make(value:int)->bool:
13            left_count= index
14            right_count= n-index-1
15            total= side_sum(value, left_count)+value+side_sum(value, right_count)
16            return total<=maxSum
17        
18        left=1
19        right=maxSum
20        answer = 1
21
22        while left<=right:
23            mid= (left+right)//2
24
25            if can_make(mid):
26                answer= mid
27                left= mid+1
28            else:
29                right= mid-1
30        return answer