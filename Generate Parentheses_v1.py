class Solution:
    def generateParenthesis(self, n: int):
        if n == 1:
            return ["()"]
        elif n == 0:
            return None
        res = []
        def backtrack(s='', left=0, right=0):
            if len(s) == 2*n:
                res.append(s)
                return
            if left < n:
                backtrack(s+'(', left+1, right)
            if right < n and right < left:
                backtrack(s + ')', left, right+1)

        backtrack()
        return res

s = Solution()
res = s.generateParenthesis(3)
print(res)
