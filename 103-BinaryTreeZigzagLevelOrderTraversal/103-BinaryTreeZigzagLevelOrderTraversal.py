# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        flag=True
        if not root:
            return []
        result=[]
        q= deque([root])

        while q:
            size= len(q)
            curr_set = []
            for  _ in range(size):
                if flag:
                    node = q.popleft()
                    if node:
                        curr_set.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    node = q.pop()
                    if node:
                        curr_set.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
            result.append(curr_set)
            flag = not flag
        return result

        
        

