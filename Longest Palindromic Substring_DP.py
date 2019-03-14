class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.is_palindromic(s):
            return s
        n = len(s)
        res = s[0]
        dp = [[1]*n for _ in range(n-1)]
        for j in range(1, n):
            for i in reversed(range(0,j)):
        # for i in range(0,n):
        #     for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i < 2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    if j-i+1 > len(res) and dp[i][j]:
                        res = s[i:j+1]
                else:
                    dp[i][j] = 0

        # print(dp)
        return res

    def is_palindromic(self, s: str):
        if s == s[::-1]:
            return True
        return False


s = Solution()

res = s.longestPalindrome("abcda")
print(res)
res = s.longestPalindrome('babad')
print(res)
res = s.longestPalindrome('cbbd')
print(res)



