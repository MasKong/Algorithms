class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            inter =  self.twoSum(nums[i+1:], -nums[i])
            if inter:
                for j in inter:
                    j.insert(0, nums[i])
                    if j not in res:
                        res.append(j)
        return res


    def twoSum(self, nums, target):
        i = 0
        j = len(nums)-1
        res = []
        while i < j:
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return res

s = Solution()
res = s.threeSum([-1, 0, 1, 2, -1, -4])
print(res)
s = Solution()
res = s.threeSum([-2,0,1,1,2])
print(res)


