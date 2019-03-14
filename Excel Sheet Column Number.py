class Solution:
    def titleToNumber(self, s):
        """
        :type n: int
        :rtype: str
        """
        count = 0
        for i in range(len(s)-1, -1, -1):
            count += (ord(s[i]) - ord('A')+1) * 26 ** (len(s)-i-1)
            # print(ord(s[i]))
            # print((len(s)-i))
        return count

s = Solution()
re1 = s.titleToNumber('ZY')
print(re1)
re2 = s.titleToNumber("AA")


print(re2)



