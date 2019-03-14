class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums:
            return []
        if len(nums) == k:
            return [max(nums)]
        if k == 1:
            return nums
        res = []
        for i in range(0, len(nums)-k+1):
            arr = nums[i:i+k]
            if not res:
                cur = self.index_max_elem(arr) + i
                res.append(arr[cur])
            elif arr[-1] > res[-1]:
                res.append(nums[i:i+k][-1])
            elif cur in range(i, i+k):
                res.append(res[-1])
            else:
                cur = self.index_max_elem(arr) + i
                res.append(nums[cur])
        return res

    def index_max_elem(self, l):
        '''find the index of the max element in a list'''
        return max(range(len(l)), key=lambda x:l[x])




s = Solution()
# print(s.index_max_elem([2,4]))
res = s.maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3)
print(res)
res = s.maxSlidingWindow(nums=[1,3], k=2)
print(res)
res = s.maxSlidingWindow(nums=[7,2,4], k=2)
print(res)
