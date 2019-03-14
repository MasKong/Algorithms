# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sort(self, head):   #naive version
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if head is None:
            return None
        cur = head
        count = 0
        while cur is not None:
            if cur.val % 2 != count % 2:
                idiot = cur.next
                while idiot is not None and idiot.val % 2 != count % 2:
                    idiot = idiot.next
                if idiot is None:
                    return None
                else:
                    cur.val, idiot.val = idiot.val, cur.val

            count += 1
            cur = cur.next
            # if cur.val % 2 == count % 2:



from utils import make_linked_list, print_linked_list, ListNode
s = Solution()
l = [2,1,3,5,6,4,7]
input_l = make_linked_list(l)
h = s.sort(input_l)
print_linked_list(h)



