# # class Solution:
# def maxSubArray(nums):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: float
#     """
#     if len(nums) == 1:
#         return nums[0]
#     l = [nums[0]]
#     if nums[0] == 0:
#         k = 1
#     else:
#         k = 0
#     # last = 0
#     for i in range(1,len(nums)):
#         # if nums[i] <0:
#
#         # else:
#         #     k = 0
#         if k > 3:
#             for j in range(i-2,i):
#
#             # l.append(maxSubArray([i-3:i+1]))
#             k = 0
#             continue
#         if l[i-1] >0:
#             # if nums[i-1]>0:
#             #     k = 0
#             # if l[i-1]>l[i-2]:
#             #     k = 0
#             l.append(nums[i] + l[i-1])
#             if nums[i] == 0:
#                 k += 1
#         else:
#             l.append(nums[i])
#             if nums[i] == 0:
#                 k=1
#             else:
#                 k = 0
#     print(l)
#     return max(l)
#             # else:
#
#
# # leg = maxSubArray([0,2,0,0,0,16,0,0,0])
# leg = maxSubArray([1,2,3,4,5])
# leg = maxSubArray([15,0,0,0,0,20])
# leg = maxSubArray([15,0,1,-5,0,0,1,0,20])
#
# print(leg)
#
#
#
#
