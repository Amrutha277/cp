# Last updated: 3/12/2026, 2:37:52 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left=0
4        right=len(height)-1
5        max_water= 0
6
7        while left<right:
8            width= right-left
9            cur_height= min(height[left], height[right])
10            cur_area= width * cur_height
11
12            max_water = max(max_water, cur_area)
13
14            if height[left]<height[right]:
15                left+=1
16            else:
17                right-=1
18        return max_water