class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(0,prices[-1] - prices[0] - fee)
        result = [prices[1] - prices[0] - fee]
        for i in range(2, len(prices)):
            if result[-1] < 0:
                result.append(max(prices[i] - prices[0] - fee, prices[i] - prices[i-1] - fee))
            # elif len(result)>1 and result[-1] - result[-2] > 0:
            elif prices[i-1] - prices[i-2] > 0:  # price increase continuously
                # if prices[i] - prices[i-1] > 0:
                #     result.append(result[-1] + prices[i] - prices[i - 1])
                '''prices[i] - prices[0] - fee :buy at beginning and sell finally
                result[-1] + prices[i] - prices[i-1] - fee : privious optimal + buy and sell 
                result[-1] L previously optimal'''
                result.append(max(prices[i] - prices[0] - fee,
                                  result[-1] + prices[i] - prices[i - 1], result[-1]))
            else:
                result.append(max(prices[i] - prices[0] - fee,
                                  result[-1] + prices[i] - prices[i-1] - fee, result[-1]))

        print(result)
        return max(result[-1], 0)


s = Solution()
re1 = s.maxProfit([1, 3, 2, 8, 4, 9], 2)
print(re1)

re2 = s.maxProfit([1,4,6,2,8,3,10,14], 3)
print(re2)

re3 = s.maxProfit([4,5,2,4,3,3,1,2,5,4], 1)
print(re3)

re4 = s.maxProfit([1,3,7,5,10,3], 3)
print(re4)

re5 = s.maxProfit([3,1,2,10,3, 100, 90, 150], 1)
print(re5)
