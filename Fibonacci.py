# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

s = Solution()
res = s.Fibonacci(38)
print(res)

