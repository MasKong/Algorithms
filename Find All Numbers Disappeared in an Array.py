class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        print(nums)
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


s = Solution()
res = s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(res)
# res = f(-1,4,15)
# print(res)
# res = f(0,-1,5)
# print(res)


