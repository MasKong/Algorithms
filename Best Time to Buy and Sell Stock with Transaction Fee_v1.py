class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        state = profit = 0
        last_price = prices[0]
        for p in prices[1:]:
            state += p - last_price
            if state > fee:
                profit += state - fee
                state = fee
            else:
                if state < 0: state = 0
            last_price = p
        return profit




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
