# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None:
            return None
        p = head
        p1 = p
        count = 0
        while count < k:
            p1 = p1.next
            count += 1
            if p1 is None and count < k:
                return None
        while p1 is not None:
            p = p.next
            p1 = p1.next
        return p

s = Solution()
from utils import make_linked_list
head = make_linked_list([1,2,3,4,5])
res = s.FindKthToTail(head, 1)
print(res)
head = make_linked_list([1,2,3,4,5,6])
res = s.FindKthToTail(head, 3)
print(res)
head = make_linked_list([1,2,3,4,5,6])
res = s.FindKthToTail(head, 10)
print(res)
res = s.FindKthToTail(None, 3)
print(res)
head = make_linked_list([1,2,3,4,5,6])
res = s.FindKthToTail(head, 1)
print(res)
head = make_linked_list([1,2,3,4,5,6])
res = s.FindKthToTail(head, 6)
print(res)