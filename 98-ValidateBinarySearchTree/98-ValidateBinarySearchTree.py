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

        # def inorder(node):
        #     if not node:
        #         return 

        #     inorder(node.left)
        #     result.append(node.val)
        #     inorder(node.right)

        # inorder(root)
        # # return result

        # for i in range(1, len(result)):
        #     if result[i]<=result[i-1]:
        #         return False
        # return True

        self.prev= None #self. so that it can be accessed across functions

        def inorder(node):
            if not node:
                return True
            
            if not inorder(node.left):
                return False

            if self.prev is not None and self.prev>= node.val:
                return False
            
            self.prev= node.val
            if not inorder(node.right):
                return False
            return True

        return inorder(root)


        