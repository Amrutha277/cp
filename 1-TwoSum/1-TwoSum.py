# Last updated: 3/11/2026, 3:19:48 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        prev_map= {}
4        for i, n in enumerate(nums):
5            complement= target-n
6
7            if complement in prev_map:
8                return [prev_map[complement],i]
9            prev_map[n]=i