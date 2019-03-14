class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        if len(s) == 1:
            return s
        for i in range(0,len(s)-1):
            for j in range(i+1, len(s)+1):
                if self.is_palindromic(s[i:j]) and j-i > len(res):
                    res = s[i:j]

        # i = 0
        # j = 1

        # while j < len(s)+1:
        #     if self.is_palindromic(s[i:j]):
        #         if j-i > len(res):
        #             res = s[i:j]
        #         j += 1
        #     else:
        #         i += 1
        #         j = i + 1

        return res

    def is_palindromic(self, s: str):
        if s == s[::-1]:
            return True
        return False


s = Solution()
res = s.longestPalindrome('babad')
print(res)
res = s.longestPalindrome('cbbd')
print(res)



