# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        res = root.val
        l = [(root, root.val)]
        while l:
            cur = l.pop()

            if cur[0].right is not None:
                l.append((cur[0].right, cur[0].right.val+cur[1]))
            elif cur[0].left is not None:
                l.append((cur[0].left, cur[0].left.val+cur[1]))
            else:
                if cur[1] == sum:
                    return True
        return False





