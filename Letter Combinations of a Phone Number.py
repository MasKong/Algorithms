class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        n=len(digits)
        if n==0:
            return []
        mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        l = []
        for item in mapping[digits[0]]:
            l.append(item)
        for i in range(1,n):
            record = len(l)
            for item in mapping[digits[i]]:
                for j in range(record):
                    idiot = l[j]+item
                    l.append(idiot)
            l = l[record:]
        return l

s = Solution()
result1 = s.letterCombinations('23')
print(result1)







