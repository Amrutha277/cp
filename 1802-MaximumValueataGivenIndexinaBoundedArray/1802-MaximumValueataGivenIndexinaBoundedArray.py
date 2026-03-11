# Last updated: 3/10/2026, 8:37:20 PM
1class Solution:
2    def maxValue(self, n: int, index: int, maxSum: int) -> int:
3        def get_sum(h,length):
4            if length ==0:
5                return 0
6            if h>=length:
7                return (h+h-length+1)*length //2
8            else:
9                return (h+1)*h//2 + (length-h)
10        
11        left, right= 1, maxSum
12        ans=1
13
14        while left<=right:
15            mid= (left+right)//2
16
17            total_sum= mid+ get_sum(mid-1, index) + get_sum(mid-1, n-1-index)
18
19            if total_sum <= maxSum:
20                ans= mid
21                left = mid+1
22            else:
23                right= mid-1
24        return ans