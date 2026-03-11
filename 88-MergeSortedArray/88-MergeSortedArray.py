# Last updated: 3/11/2026, 3:11:55 PM
1class Solution(object):
2    def merge(self, nums1, m, nums2, n):
3        """
4        :type nums1: List[int]
5        :type m: int
6        :type nums2: List[int]
7        :type n: int
8        :rtype: None Do not return anything, modify nums1 in-place instead.
9        """
10        p1= m-1
11        p2= n-1
12        p= m+n-1
13
14        while p1>=0 and p2>=0:
15            if nums1[p1]>nums2[p2]:
16                nums1[p]= nums1[p1]
17                p1-=1
18            else:
19                
20                nums1[p]= nums2[p2]
21                p2-=1
22            p-=1
23        while p2>=0:
24            nums1[p]= nums2[p2]
25            p2-=1
26            p-=1
27
28        
29
30
31
32
33