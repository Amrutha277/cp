# Last updated: 7/24/2025, 4:33:35 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if all(x>0 for x in asteroids) or all(x<0 for x in asteroids):
            return asteroids
        stack=[]
        for ast in asteroids:
            if ast>0:
                stack.append(ast)
            else:
                # print(stack[-1])
                alive= True
                while stack and ast<0 and stack[-1]>0:
                    if (-1*ast) > stack[-1]:
                        stack.pop()
                        continue  #break the smaller ast
                    elif (-1*ast) == stack[-1]:
                        stack.pop()  #
                        alive= False
                        print(stack)
                        break  #both are destroyed. so while loop shld also be exited
                    else:
                        alive= False
                        break
                if alive:
                    stack.append(ast)
                
        return stack
            
                
