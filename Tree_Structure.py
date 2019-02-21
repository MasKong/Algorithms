# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):

    @classmethod
    def build_tree(self, l):
        l_node = list(map(TreeNode, l))
        for i in range(1,len(l_node)):
            if not l_node[i].val:
                continue
            if i % 2 == 1:
                # print(int((i-1)/2))
                l_node[int((i-1)/2)].left = l_node[i]
            else:
                # print(int((i - 2) / 2))
                l_node[int((i - 2) / 2)].right = l_node[i]
        return l_node[0]

    @classmethod
    def Pre_Order_Traversal(self, root):
        '''DFS Recursion'''
        if not root:
            return []
        result = []
        def recurse_post_order(node):
            if node:
                result.append(node.val)
                if node.left:
                    recurse_post_order(node.left)
                if node.right:
                    recurse_post_order(node.right)
        recurse_post_order(root)
        return result



    @classmethod
    def In_Order_Traversal(self, root):
        '''DFS Recursion'''
        if not root:
            return []
        result = []
        def recurse_post_order(node):
            if node:
                if node.left:
                    recurse_post_order(node.left)
                result.append(node.val)
                if node.right:
                    recurse_post_order(node.right)

        recurse_post_order(root)
        return result

    @classmethod
    def BFS_Traversal(self, root):
        '''BFS, print the result directly. Use list as a queue,
        not efficient'''
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            record = len(queue)
            for i in range(record):
                current = queue[i]
                result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            queue = queue[record:]
        return result

    @classmethod
    def Post_Order_Traversal(self, root):
        '''DFS Recursion'''
        if not root:
            return []
        result = []
        def recurse_post_order(node):
            if node:
                if node.right:
                    recurse_post_order(node.right)
                if node.left:
                    recurse_post_order(node.left)
                result.append(node.val)
        recurse_post_order(root)
        return result

tree = Tree()
root_node = tree.build_tree([1,2,3,None,5,None,4,None, None, 20])
# print(root_node.left)
# result = tree.In_Order_Traversal(root_node)
# # print(result)
# # re1 = tree.In_Order_Print(root_node)
# # print(re1)
re2 = tree.Post_Order_Traversal(root_node)
print(re2)
re3 = tree.Pre_Order_Traversal(root_node)
print(re3)
re4 = tree.In_Order_Traversal(root_node)
print(re4)
