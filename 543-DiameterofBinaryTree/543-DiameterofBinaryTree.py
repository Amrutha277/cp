# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        diameter = [0]
        self.height(root, diameter)
        return diameter[0]

    def height(self, node, diameter):
        if not node:
            return 0

        lh= self.height(node.left, diameter)
        rh= self.height(node.right, diameter)

        diameter[0]= max(diameter[0],lh+rh)

        return 1+max(lh,rh)
    
