# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque, defaultdict
    # import heapq
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # node_map = defaultdict(list)
        # def dfs(node, x, y):
        #     if not node:
        #         return
        #     heapq.heappush(node_map[x], (y, node.val))
        #     dfs(node.left, x-1, y-1)
        #     dfs(node.right, x+1, y-1)
        
        # dfs(root, 0,0)

        # result=[]
        # for x in sorted(node_map.keys()):
        #     column = [val for y, val in sorted(node_map[x], key=lambda p:(-p[0], p[1]))]
        #     result.append(column)
        
        # return result
        
        if not root:
            return []
        
        node_map = defaultdict(list)
        queue = deque([(root, 0,0)])

        while queue:
            node, x,y = queue.popleft()
            node_map[x].append((y,node.val))

            if node.left:
                queue.append((node.left, x-1, y-1))
            if node.right:
                queue.append((node.right, x+1, y-1))
            
        result = []
        for x in sorted(node_map.keys()):
            column = [val for y, val in sorted(node_map[x], key = lambda p: (-p[0],p[1]))]
            result.append(column)
        
        return result
