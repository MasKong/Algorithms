class Solution:
    def letterCombinations(self, digits: str):
        n = len(digits)
        if n == 0:
            return []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if n == 1:
            return list(mapping[digits])
        prev = self.letterCombinations(digits[:-1])
        last = list(mapping[digits[-1]])
        return [s+c for s in prev for c in last]


s = Solution()
res = s.letterCombinations("23")
print(res)


