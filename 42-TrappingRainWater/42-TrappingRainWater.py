# Last updated: 7/23/2025, 1:57:58 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        nge={}
        stack=[]
        area=0
        for i in range(len(height)):
            # print("i=", i)
            while stack and height[i]>=height[stack[-1]]:
                bottom= stack.pop()
                if not stack:
                    break
                width= i- stack[-1]-1
                water_height = min(height[i], height[stack[-1]]) - height[bottom]
                area+= width * water_height
                # print( left, i, area)
            stack.append(i)
            
        return area
