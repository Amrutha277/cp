# Last updated: 3/11/2026, 4:23:35 PM
1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        def find_bound(is_left):
4            left, right= 0, len(nums)-1
5            bound = -1
6
7            while left<=right:
8                mid= (left+right)//2
9                if nums[mid] == target:
10                    bound= mid
11                    if is_left:
12                        right= mid-1
13                    else:
14                        left= mid+1
15                elif nums[mid]<target:
16                    left= mid+1
17                else:
18                    right = mid-1
19            return bound
20        return [find_bound(True), find_bound(False)]