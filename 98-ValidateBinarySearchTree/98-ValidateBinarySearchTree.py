# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # if root.left:
        #     if root.left.val >= root.val:
        #         return False
        #     else:
        #         self.isValidBST( root.left)
        # if root.right:
        #     if root.right.val<= root.val:
        #         return False
        #     else:
        #         self.isValidBST( root.right)
        
        # return True
        result=[]
        def inorder(node):
            if not node:
                return 

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        # return result

        for i in range(1, len(result)):
            if result[i]<=result[i-1]:
                return False
        return True



        