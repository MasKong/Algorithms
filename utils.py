# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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