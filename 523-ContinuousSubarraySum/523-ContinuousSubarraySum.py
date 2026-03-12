# Last updated: 3/12/2026, 2:57:28 PM
1class Solution:
2    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
3        remainder_map= {0:-1}
4
5        running_sum= 0
6
7        for i, n in enumerate(nums):
8            running_sum+=n
9            remainder= running_sum%k
10
11            if remainder in remainder_map:
12                if i - remainder_map[remainder]>1:
13                    return True
14            else:
15                remainder_map[remainder]=i
16        return False