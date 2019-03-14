# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):   #naive version
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        i = 0
        n = len(lists)
        while i < n:
            if lists[i] is None:
                del lists[i]
                n = len(lists)
            else:
                i += 1
        cur_l = sorted(lists, key=lambda i:i.val)
        if len(lists) == 0:
            return None
        head = cur_l[0]
        p = head
        if cur_l[0].next is not None:
            cur_l[0] = cur_l[0].next
        else:
            del cur_l[0]
        self.sort_l(cur_l)
        while cur_l:
            p.next = cur_l[0]
            p = p.next
            if cur_l[0].next is None:
                del cur_l[0]
            else:
                cur_l[0] = cur_l[0].next
                self.sort_l(cur_l)
        return head

    def sort_l(self, cur_l):
        '''cur_l is a list and the first node is with the minimum value'''
        cur = 0
        for i in range(1, len(cur_l)):
            if cur_l[cur].val > cur_l[i].val:
                # if i==1:
                #     break
                # else:
                cur_l[cur], cur_l[i] = cur_l[i], cur_l[cur]
                cur = i
                # cur = cur_l[i]
        # cur_l[0], cur_l[len(cur_l)-1] = cur_l[len(cur_l)-1], cur_l[0]



# from utils import make_linked_list, print_linked_list, ListNode
# s = Solution()
# l = [1,4,5]
# l1 = [1,3,4]
# l2 = [2,6]
# input_l = list(map(make_linked_list,[l,l1,l2]))
# h = s.mergeKLists(input_l)
# print_linked_list(h)



