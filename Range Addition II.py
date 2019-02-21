class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        l = [[0 for _ in range(n)] for _ in range(m)]
        # print(l)
        for item in ops:

            for i in item[0]:
                for j in item[1]:
                    l[i][j] += 1

        



s = Solution()
re1 = s.maxCount(3,3,[[2,2],[3,3]])
print(re1)




