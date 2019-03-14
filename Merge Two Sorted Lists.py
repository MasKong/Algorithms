# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        if cur1 is None:
            return cur2
        elif cur2 is None:
            return cur1

        if cur1.val < cur2.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next
        p = head
        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                p.next = cur1
                cur1 = cur1.next
                p = p.next
            else:
                p.next = cur2
                cur2 = cur2.next
                p = p.next
        if cur1 is None:
            p.next = cur2
        elif cur2 is None:
            p.next = cur1
        return head







def make_linked_list(l):
    if not l:
        return None
    head = ListNode(l[0])
    cur = head
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
    return head

def print_linked_list(head):
    if head is None:
        print(None)
    else:
        cur = head
        while cur is not None:
            print(cur.val)
            # print("->")
            cur = cur.next


l1 = make_linked_list([1,2,4])
l2 = make_linked_list([1,3,4])
s = Solution()
res = s.mergeTwoLists(l1, l2)
print_linked_list(res)
