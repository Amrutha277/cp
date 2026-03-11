# Last updated: 3/11/2026, 4:49:47 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        results= []
5        n= len(nums)
6
7        for i in range(n-3):
8            if i>0 and nums[i] == nums[i-1]:
9                continue
10            for j in range(i+1, n-2):
11                if j>i+1 and nums[j] == nums[j-1]:
12                    continue
13                
14                left = j+1
15                right= n-1
16
17                while left<right:
18                    curr_sum = nums[i]+nums[j]+nums[left]+nums[right]
19                    if curr_sum == target:
20                        results.append([nums[i], nums[j], nums[left], nums[right]])
21
22                        while left<right and nums[left] == nums[left+1]:
23                            left+=1
24                        while left<right and nums[right] == nums[right-1]:
25                            right-=1
26                        
27                        left+=1
28                        right-=1
29                    elif curr_sum<target:
30                        left+=1
31                    else:
32                        right-=1
33        return results
34
35
36