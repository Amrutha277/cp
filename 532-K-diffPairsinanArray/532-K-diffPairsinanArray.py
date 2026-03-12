# Last updated: 3/12/2026, 4:22:49 PM
1from collections import Counter
2class Solution:
3    def findPairs(self, nums: List[int], k: int) -> int:
4        count_map=Counter(nums)
5        unique_pairs= 0
6
7        for x in count_map:
8            if k>0:
9                if x+k in count_map:
10                    unique_pairs+=1
11            else:
12                if count_map[x]>1:
13                    unique_pairs+=1
14        return unique_pairs