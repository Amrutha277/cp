# Last updated: 3/12/2026, 1:38:46 PM
1class Solution:
2    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
3        rank= [[0]*n for _ in range(n)]
4        for i in range(n):
5            for r, friend in enumerate(preferences[i]):
6                rank[i][friend]=r
7            
8        partner=[0]*n
9        for u,v in pairs:
10            partner[u]= v
11            partner[v]=u
12        
13        unhappy_count=0
14
15        for x in range(n):
16            y= partner[x]
17            current_rank_for_x = rank[x][y]
18
19            is_unhappy= False
20
21            for u in preferences[x]:
22                if rank[x][u]>= current_rank_for_x:
23                    break
24                
25                v= partner[u]
26                if rank[u][x]<rank[u][v]:
27                    is_unhappy= True
28                    break
29            if is_unhappy:
30                unhappy_count+=1
31        return unhappy_count
32            
33
34