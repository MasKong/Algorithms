# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        l = []
        p = pHead
        while p is not None:
            l.append(p.val)
            p = p.next
        head = ListNode(l[-1])
        p = head
        if len(l) > 1:
            for i in range(len(l)-2, -1, -1):
                p.next = ListNode(l[i])
                p = p.next
        return head
