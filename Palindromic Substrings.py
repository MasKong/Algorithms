class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        for i in range(0, len(s)):
            for j in range(i+1,len(s)+1):
                if self.is_palindromic(s[i:j]):
                    res.append(s[i:j])
        return len(res)

    def is_palindromic(self, s: str):
        if s == s[::-1]:
            return True
        return False
        # if len(s) == 0:
        #     return True
        # for i in range(int(len(s)/2)):
        #     if s[i] != s[len(s)-1-i]:
        #         return False
        # return True


s = Solution()
res = s.countSubstrings("aba")
print(res)
res = s.countSubstrings("abc")
print(res)
res = s.countSubstrings("aaa")
print(res)


