# -*- coding:utf-8 -*-
class Solution:
    def replaceSpace(self, s):
        if not s:
            return ""
        else:
            res = ""
            n = len(s)
            for i in range(0, n):
                if s[i] == ' ':
                    res += "%20"
                else:
                    res += s[i]
        return res


s = Solution()
res = s.replaceSpace("We Are Happy")
print(res)
s = Solution()
res = s.replaceSpace("hello world")
print(res)
s = Solution()
res = s.replaceSpace(" helloworld")
print(res)


