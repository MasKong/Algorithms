# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return list(self.traverse(l2))
        elif l2 is None:
            return list(self.traverse(l1))
        return list(map(lambda i:int(i), list(str(int(self.traverse(l1)) + int(self.traverse(l2)))[::-1])))


    def traverse(self, l1):
        res = ''
        cur = l1
        while cur is not None:
            res += str(cur.val)
            cur = cur.next
        return res[::-1]


s = Solution()
# res = s.addTwoNumbers((2 -> 4 -> 3) + (5 -> 6 -> 4))
# print(res)