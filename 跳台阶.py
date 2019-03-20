# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 1:
            return 0
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            l = [1, 2]
            # n = 1
            # m = 2
            for i in range(3, number+1):
                l.append(l[-1]+l[-2])
            # print(l)
            return l[-1]

s = Solution()
res = s.jumpFloor(0)
print(res)
res = s.jumpFloor(1)
print(res)
res = s.jumpFloor(2)
print(res)
res = s.jumpFloor(3)
print(res)
res = s.jumpFloor(4)
print(res)
res = s.jumpFloor(20)
print(res)