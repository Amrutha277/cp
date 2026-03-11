# Last updated: 3/10/2026, 9:14:14 PM
1from collections import defaultdict
2class Solution:
3    def invalidTransactions(self, transactions: List[str]) -> List[str]:
4        parsed=[]
5        for t in transactions:
6            name, time, amount, city= t.split(',')
7            parsed.append({
8                "name":name,
9                "time": int(time),
10                "amount":int(amount),
11                "city":city,
12                "raw":t
13            })
14        
15        invalid_indices= set()
16
17        for i in range(len(parsed)):
18            if parsed[i]["amount"]>1000:
19                invalid_indices.add(i)
20            for j in range(len(parsed)):
21                if i == j:
22                    continue
23                
24                if (parsed[i]["name"] == parsed[j]["name"] and 
25                    parsed[i]["city"] != parsed[j]["city"] and
26                    abs(parsed[i]["time"] - parsed[j]["time"]) <=60):
27
28                    invalid_indices.add(i)
29                    break
30        return [parsed[i]["raw"] for i in invalid_indices]
31