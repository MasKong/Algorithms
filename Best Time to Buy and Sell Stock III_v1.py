class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        l = [0]
        r = [0]*(len(prices))
        min_price = prices[0]
        max_price = prices[-1]
        for i in range(1,len(prices)):
            l.append(max(l[i-1],prices[i] - min_price))
            min_price = min(min_price, prices[i])
        for j in range(len(prices)-2,0,-1):
            # print(j)
            # print(len(l))
            r[j] = max(r[j+1],max_price - prices[j+1])
            max_price = max(max_price, prices[j])
        result = 0
        for i in range(len(prices)):
            result = max(result, l[i]+r[i])
        return result
s = Solution()
leg = s.maxProfit([1,2,3,4,5])
# leg = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# leg = s.max_cross([-2,1,-3,4,-1,2,1,-5,4])

print(leg)
