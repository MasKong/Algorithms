# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            index_h = tin.index(pre[0])
            head = TreeNode(pre[0])
            head.left = self.reConstructBinaryTree(pre[1:index_h+1], tin[:index_h]) #left tree
            head.right = self.reConstructBinaryTree(pre[index_h + 1:], tin[index_h+1:])  # right tree
            return head

s = Solution()
res = s.reConstructBinaryTree([1,2,4,3,5,6],[4,2,1,5,3,6])

