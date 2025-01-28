# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        sum = [float('-inf')]
        self.height(root, sum)
        return sum[0]

    def height(self, root, sum):
        if not root:
            return 0

        lsum= max(0,self.height(root.left,sum))
        rsum= max(0,self.height(root.right,sum))

        sum[0]= max(sum[0], lsum + rsum + root.val)

        return max(lsum, rsum)+root.val
    
            
            
