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
        if len(lists) == 0:
            return None
        value_l = []
        index_l = []    #store the pointer of each linked-list
        for i in range(len(lists)):
            if lists[i] is None:
                continue
            value_l.append(lists[i].val)      #add head to l
            index_l.append(lists[i])
        if len(value_l) == 0:
            return None
        min_val = min(value_l)
        pointer = ListNode(min_val)
        head = pointer
        index = value_l.index(min_val)
        if index_l[index].next is not None:
            index_l[index] = index_l[index].next
            value_l[index] = index_l[index].val
        else:
            del(value_l[index])
            del(index_l[index])
        while len(value_l)>0:
            min_val = min(value_l)
            pointer.next = ListNode(min_val)
            pointer = pointer.next
            index = value_l.index(min_val)
            if index_l[index].next is not None:
                index_l[index] = index_l[index].next
                value_l[index] = index_l[index].val
            else:
                del (value_l[index])
                del (index_l[index])
        return head

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