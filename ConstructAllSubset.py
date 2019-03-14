# class Solution:
#     def constructallsubset(self, nums, t):
#         if not nums or t < 0:
#             return None
#         if t == 0:
#             return []
#
#         res = []
#         y = self.constructallsubset(nums[:-1], t)
#         if y is not None:
#             res.extend(y)
#         y = self.constructallsubset(nums[:-1], t - nums[-1])
#         if y is not None:
#             y = list(map(lambda i:i.append(nums[-1]), y))
#             res.extend(y)
#         if res:
#             return None
#         return res
#
#
#
# s = Solution()
# # res = s.constructallsubset([3,2,3,1,2,4,5,5,6,0], 1000)
# # print(res)
# res1 = s.constructallsubset([3,2,1,5,6,4], 5)
# print(res1)
#
#
#
# class Solution:
#     def constructsubset(self, nums, t):
#         if not nums or t < 0:
#             return None
#         if t == 0:
#             return []
#
#
#         y = self.constructsubset(nums[:-1], t)
#         if y is not None:
#             return y
#         y = self.constructsubset(nums[:-1], t - nums[-1])
#         if y is not None:
#             y.append(nums[-1])
#             return y
#         return None
#
#
#
# s = Solution()
# res = s.constructsubset([3,2,3,1,2,4,5,5,6,0], 1000)
# print(res)
#
# l = [3,2,1,5,6,4]
# l.sort()
# res1 = []
# for i in range(len(l),0,-1):
#     res1.append(s.constructsubset(l[:i], 5))
# # res1 =
# print(res1)








