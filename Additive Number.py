class Solution:
    def isAdditiveNumber(self, num: 'str') -> 'bool':
        # for i in range(3, len(num)):
        if len(num) == 3 and int(num[0]) + int(num[1]) == int(num[2]):
            return True

        i = 3
        if self.isAdditiveNumber(num[:i]):
            if len(num) - 1 < 3:
                return True
            return self.isAdditiveNumber(num[1:])
        else:
            for i in range(4, len(num)):
                if self.isAdditiveNumber(num[:i]):
                    return self.isAdditiveNumber(num[1:])
            return False

    def match(self, num):
        res = []
        for i in range(0, len(num)-1):
            if int(num[:i]) == n:
                return i
        return False



s = Solution()
res = s.isAdditiveNumber('112358')
print(res)
res = s.isAdditiveNumber('199100')
print(res)
res = s.isAdditiveNumber('1121325')
print(res)
res = s.isAdditiveNumber('199100199')
print(res)


