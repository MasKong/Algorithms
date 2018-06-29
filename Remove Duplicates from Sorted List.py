# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node!=None:
            if node.next == None:
                return head
            while node.val == node.next.val:
                node.next = node.next.next
                if node.next == None:
                    return head
            node = node.next

s = Solution()
# leg = s.maxSubArray([-1,2,3,-6,8])

# leg = s.max_cross([-2,1,-3,4,-1,2,1,-5,4])
# a = "anagram"
# b = "nagaram"
# a = "aacc"
# b = "accc"
# leg = s.isPalindrome("A man, a plan, a canal: Panama")
# print(leg)

