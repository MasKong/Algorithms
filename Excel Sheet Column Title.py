class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # import math
        # n_p = math.log(n, 26)
        # print(n_p)
        # return self.convertToTitle((n - 1) / 26) + chr((n - 1) % 26 + ord('A'))
        return "" if n == 0 else self.convertToTitle(int((n - 1) / 26)) + chr(int((n  - 1) % 26) + ord('A'))

s = Solution()
re1 = s.convertToTitle(701)
re2 = s.convertToTitle(2)

print(re1)
print(re2)



