# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''BFS'''
        if not root:
            return []
        l = [root]
        result = []
        # node = root
        while l:
            intermediate = []
            record = len(l)
            for i in range(record):
                node = l[i]
                intermediate.append(node.val)
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            result.append(intermediate[-1])
            l = l[record:]

        return result