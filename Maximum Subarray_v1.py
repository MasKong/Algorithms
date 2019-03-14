class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 1:
            return nums[0]
        l = [nums[0]]
        for i in range(1,len(nums)):
            # if nums[i] <0:
            if l[i-1] >0:
                l.append(nums[i] + l[i-1])
            else:
                l.append(nums[i])
        ind = l.index(max(l))
        res = []
        for i in range(ind, -1, -1):
            if l[i] > 0:
                res.append(nums[i])
            else:
                break
        return res[::-1]
            # else:



s = Solution()
res = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)
s = Solution()
res = s.maxSubArray([-3,10,6,0,-1,19,-15,11,3,-27,18])
print(res)

