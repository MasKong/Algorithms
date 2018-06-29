# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        if head == None:
            return None
        if head.next == None:
            return head
        if head.next.val != head.val:   #the first two elements are not the same
            current_node = node         # this is the same as the later except that whether
            node = node.next            #the first few elements are the same
            while node != None:
                if node.next == None:
                    current_node.next = node
                    return head
                if node.next.val != node.val:
                    current_node.next = node
                    current_node = node
                else:   # when next node is the same as the current node
                    while node != None:
                        if node.next == None:
                            current_node.next = None
                            return head
                        else:
                            node = node.next
                        if node.next == None:
                            current_node.next = None
                            return head
                        if node.val != node.next.val:
                            break


                node = node.next

            # while node != None:
            #     if node.next == None:
            #         return head
            #     if node.next.val != node.val:
            #         current_node.next = node
            #     else:
            #         while node != None:
            #             if node.next == None:
            #                 current_node.next = None
            #                 return head
            #             else:
            #                 node = node.next
            #             if node.val != node.next.val:
            #                 break

                # if node.next.val == node.val:
                #     value = node.val
                #
                #     while node.next != None:
                #         node = node.next
                #         if node.val != value:
                #             current_node.next = node
                # else:
                #     current_node = node
                # node = node.next



        else:
            current_node = None     #the first two elements are same, pointers point to None
            while node != None:
                if node.next == None:
                    if current_node == None:    # all elements includes the first few elements are same
                        return node             #return None
                    current_node.next = node    #add the last node to the linked list
                    return head
                if node.next.val != node.val:   #current node is to record the last node in the linked list
                    if current_node == None:    #which is identical in the list
                        current_node = node
                        head = current_node
                    else:
                        current_node.next = node
                        current_node = node
                else:   # when next node is the same as the current node
                    while node != None:         # if the node is the same with next node
                        if node.next == None:   # this loop is to skip the node
                            current_node.next = None
                            return head
                        else:
                            node = node.next
                        if node.next == None:
                            if current_node == None:
                                return None
                            current_node.next = None
                            return head
                        if node.val != node.next.val:
                            break


                node = node.next

s = Solution()
l = [1,1,2]
# l = [1,2,3,3,4,4,5,5]
# l = [2,2,3,4,5,5]
LN = ListNode(l[0])
# for i in range(1,len(l)):
#     LN.next
node_list = list(map(ListNode,l))
# print(node_list[0])
# print(ListNode(l[0]))
for i in range(len(node_list)-1):
    node_list[i].next = node_list[i+1]

h = s.deleteDuplicates(node_list[0])
while h!= None:
    print(h.val)
    h = h.next

