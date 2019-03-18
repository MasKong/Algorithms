# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        p = listNode
        l = []
        if p is None:
            return []
        else:
            while p is not None:
                l.append(p.val)
                p = p.next
        return l[::-1]

# s = Solution()
# res = s.replaceSpace("We Are Happy")
# print(res)
# s = Solution()
# res = s.replaceSpace("hello world")
# print(res)
# s = Solution()
# res = s.replaceSpace(" helloworld")
# print(res)

