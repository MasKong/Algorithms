# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        a = int(self.traverse(l1))
        b = int(self.traverse(l2))
        c = str(a + b)
        head = ListNode(int(c[0]))
        cur = head
        for i in range(1, len(c)):
            cur.next = ListNode(int(c[i]))
            cur = cur.next
        cur.next = None
        return head

        # cur1 = l1
    #         # cur2 = l2
    #         # c = []
    #         # while cur1 and cur2:
    #         #     res = cur1.val + cur2.val
    #         #     if res >= 10:
    #         #         c.append(1)
    #         #         cur1.val = res % 10
    #         #     else:
    #         #         c.append(0)
    #         #         cur1.val = res
    #         #     cur1 = cur1.next
    #         #     cur2 = cur2.next
    #         # if cur1 is None and cur2 is None:
    #         #     cur1 = l1
    #         #     if c[0]:
    #         #         l1 = ListNode(1, l1)
    #         #     cur1 = l1.next
    #         #     for i in range(1, len(c)):
    #         #         if c[i]:
    #         #             cur1.val += 1
    #         # if cur1 is None:

    def traverse(self, l1):
        res = ''
        cur = l1
        while cur is not None:
            res += str(cur.val)
            cur = cur.next
        return res


