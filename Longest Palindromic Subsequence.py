class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if self.is_palindromic(s):
            return len(s)
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        # print(dp)
        for j in range(1, n):
            for i in reversed(range(0, j)):

                if s[j] == s[i]:
                    # print("i+1", i+1)
                    # print("j-1", j-1)
                    dp[i][j] = dp[i+1][j-1] + 2 if i+1 <= j-1 else 2
                else:
                    # print("i+1", i + 1)
                    # print("j-1", j - 1)
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # print(dp)
        return dp[0][-1]

    def is_palindromic(self, s: str):
        if s == s[::-1]:
            return True
        return False



s = Solution()
res = s.longestPalindromeSubseq("aaa")
print(res)
res = s.longestPalindromeSubseq("bbbab")
print(res)
res = s.longestPalindromeSubseq("cbbd")
print(res)
