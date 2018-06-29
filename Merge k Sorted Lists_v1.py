# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = []  #store all elements
        for ll in lists:
            if ll is None:
                continue
            h = ll
            while h is not None:
                l.append(h.val)
                h = h.next
        if len(l) == 0:
            return None
        l.sort()
        head = self.make_linked_list(l)
        return head

    def make_linked_list(self,l):    #for test purpose
        LN = ListNode(l[0])
        pointer = LN
        for i in range(1,len(l)):
            pointer.next = ListNode(l[i])
            pointer = pointer.next
        return LN

def make_linked_list(l):    #for test purpose
    LN = ListNode(l[0])
    pointer = LN
    for i in range(1,len(l)):
        pointer.next = ListNode(l[i])
        pointer = pointer.next
    return LN
s = Solution()
l = [1,4,5]
l1 = [1,3,4]
l2 = [2,6]
input_l = list(map(make_linked_list,[l,l1,l2]))
# h = input_l[1]
# while h!= None:
#     print(h.val)
#     h = h.next
h = s.mergeKLists(input_l)
while h!= None:
    print(h.val)
    h = h.next