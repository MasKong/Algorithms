# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here

        n = len(array)
        i = 0
        while i < n:
            if not array[i]:
                del array[i]
                n = len(array)
            else:
                i += 1
        if not array:
            return False
        if target < array[0][0] or target > array[-1][-1]:
            return False
        n = len(array)
        for i in range(n):
            # print(i)
            if target > array[i][-1] and target > array[n - 1][i]:
                continue
            else:
                if target > array[i][-1] and target < array[n-1][i]:
                    for j in range(i, n):
                        if array[j][i] == target:
                            return True
                elif target > array[n - 1][i] and target < array[i][-1]:
                    for j in range(i, n):
                        if array[i][j] == target:
                            return True
                else:
                    for j in range(i, n):
                        if array[i][j] == target:
                            return True
                        if array[j][i] == target:
                            return True

                    # return False
        return False

s = Solution()
res = s.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
print(res)
s = Solution()
res = s.Find(16,[[]])
print(res)

