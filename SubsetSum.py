class Solution:
    def subsetSum(self, nums, t):
        if not nums or t < 0:
            return False
        if t == 0:
            return True
        return self.subsetSum(nums[:-1], t-nums[-1]) or self.subsetSum(nums[:-1], t)




s = Solution()
res = s.subsetSum([3,2,3,1,2,4,5,5,6,0], 1000)
print(res)
res1 = s.subsetSum([3,2,1,5,6,4], 5)
print(res1)



