# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def recur(root):
            if not root:
                return 0
            left_h= recur(root.left)
            right_h= recur(root.right)
            if left_h == -1:
                return -1
            if right_h == -1:
                return -1
            if abs(left_h - right_h)>1:
                return -1
            return max(left_h, right_h)+1
            
        return recur(root) != -1
            


        

            
        