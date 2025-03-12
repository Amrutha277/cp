# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # og = root
        if not root:
            return TreeNode(val)
        curr= root
        while curr:
            if val < curr.val :
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
            elif val >curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
        return root
    
    def printFun(root):
        if not root:
            return 
        result= []
        result.append(root.val)
        self.printFun(root.left)
        self.printFun(root.right)
    
        return result
