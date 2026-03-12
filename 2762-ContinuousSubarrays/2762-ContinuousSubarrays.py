# Last updated: 3/12/2026, 12:43:32 PM
1from collections import deque
2class Solution:
3    def continuousSubarrays(self, nums: List[int]) -> int:
4        n= len(nums)
5
6        maxq= deque()
7        minq= deque()
8
9        left=0
10        total_subarr=0
11
12        for right in range(n):
13            while maxq and nums[maxq[-1]]<=nums[right]:
14                maxq.pop()
15            maxq.append(right)
16
17            while minq and nums[minq[-1]]>=nums[right]:
18                minq.pop()
19            minq.append(right)
20
21            while nums[maxq[0]]-nums[minq[0]]>2:
22                left+=1
23                if maxq[0]<left:
24                    maxq.popleft()
25                if minq[0]<left:
26                    minq.popleft()
27            total_subarr += (right-left+1)
28        return total_subarr
29
30