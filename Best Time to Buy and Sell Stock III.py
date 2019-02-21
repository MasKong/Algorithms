'''Time limit exceed'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<4:
            return self.maxProfit_single(prices)
        l = []
        for i in range(0, len(prices) - 1):
            l.append(prices[i + 1] - prices[i])
        # print(l)
        r = -1
        for j in range(0,len(l)-1):
            in_result = max(0,self.maxSubArray(l[:j+1])) +  max(0,self.maxSubArray(l[j+1:]))
            if in_result > r:
                r = in_result
                # print("r: ",r)
        return max(0,r)

    def maxProfit_single(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        l = []
        # print(l)
        for i in range(0, len(prices)-1):
            l.append(prices[i+1] - prices[i])
        # print(l)
        return max(0, self.maxSubArray(l))

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
        return max(l)

s = Solution()
leg = s.maxProfit([6,1,3,2,4,7])
# leg = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# leg = s.max_cross([-2,1,-3,4,-1,2,1,-5,4])

print(leg)

