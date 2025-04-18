# Last updated: 4/18/2025, 2:11:12 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        stack1 = [root] 
        stack2 = [] 

        while stack1:
            root = stack1.pop() 
            stack2.append(root) 

            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)

        while stack2:
            root = stack2.pop()
            result.append(root.val)
        
        return result
            


