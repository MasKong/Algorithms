# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         if m==0:
#             for i in range(len(nums2)):
#                 nums1[i] = nums2[i]
#         elif n!=0 and m!=0:
#             # self.move(nums1,1,m)
#             # print(nums1)
#             i,j = 0,0
#             while i<m and j<n:
#                 if nums1[i] < nums2[j]:
#
#                     #l.append(nums1[i])
#                     i +=1
#                 else:
#                     # nums1.insert(i,nums2[j])
#                     # l.append(nums2[j])
#                     self.move(nums1, i, m)
#                     nums1[i] = nums2[j]
#                     j +=1
#                     i+=1
#             if i>=m:
#                 for k in range(i+j,m+n):
#                     nums1[k] = nums2[j]
#                     j+=1
#                 # nums1.extend(nums2[j:])
#             # nums1 = nums1[:m+n-1]
#         print(nums1)
#         # nums1=nums1[:m]
#
#
#         # if m==0:
#         #     return nums2
#         # if n==0:
#         #     return nums1
#         # l = []
#         # i,j = 0,0
#         # while i<m and j<n:
#         #     if nums1[i] < nums1[j]:
#         #         #l.append(nums1[i])
#         #         i +=1
#         #     else:
#         #         nums1.insert(i,nums2[j])
#         #         # l.append(nums2[j])
#         #         j +=1
#         # if i>=m:
#         #     nums1.extend(nums2[j:])
#         # nums1 = nums1[:m+n]
#
#     def move(self, nums1, i, m):
#         for k in range(m-1,i-1,-1):
#             nums1[k+1] = nums1[k]
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
        elif n != 0 and m != 0:
            # self.move(nums1,1,m)
            # print(nums1)
            l = []
            i, j = 0, 0
            while i < m and j < n:
                if nums1[i] < nums2[j]:

                    l.append(nums1[i])
                    i += 1
                else:
                    # nums1.insert(i,nums2[j])
                    l.append(nums2[j])
                    # self.move(nums1, i, m)
                    # nums1[i] = nums2[j]
                    j += 1
            if i >= m:
                l.extend(nums2[j:])
            else:
                l.extend(nums1[i:m])

            for k in range(len(l)):
                nums1[k] = l[k]
        print(nums1)

s = Solution()
s.merge([4,5,6,0,0,0],3,[1,2,3],3)
# s.merge([4,5,6,0,0,0],3,[2,5,6],3)
# leg = s.maxSubArray([-1,2,3,-6,8])

# leg = s.max_cross([-2,1,-3,4,-1,2,1,-5,4])
# a = "anagram"
# b = "nagaram"
# a = "aacc"
# b = "accc"
# leg = s.isPalindrome("A man, a plan, a canal: Panama")
# print(leg)