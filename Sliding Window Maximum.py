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
            res.append(max(nums[i:i+k]))
        return res




s = Solution()
res = s.maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3)
print(res)
res = s.maxSlidingWindow(nums=[1,3], k=2)
print(res)
