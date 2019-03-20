# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = n &(n-1)
            count += 1
        return count



s = Solution()
res = s.NumberOf1(0)
print(res)
res = s.NumberOf1(1)
print(res)
res = s.NumberOf1(-1)
print(res)
res = s.NumberOf1(6)
print(res)
res = s.NumberOf1(-6)
print(res)
