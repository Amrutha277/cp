# Last updated: 3/12/2026, 2:13:57 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n1,n2= len(s1), len(s2)
4        if n1>n2:
5            return False
6        
7        s1_count= [0]*26
8        window_count= [0]*26
9
10        for i in range(n1):
11            s1_count[ord(s1[i])- ord('a')]+=1
12            window_count[ord(s2[i])-ord('a')]+=1
13        
14        for i in range(n1,n2):
15            if s1_count== window_count:
16                return True
17            
18            window_count[ord(s2[i])-ord('a')]+=1
19            window_count[ord(s2[i-n1])-ord('a')]-=1
20        
21        return s1_count== window_count