class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0

        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        if len(s) == 1:
            return roman[s]
        res = 0
        i = 0
        j = 1
        n = len(s)
        while j < n:
            scale = roman[s[j]] / roman[s[i]]
            if  scale == 10 or scale == 5:
                res += roman[s[j]] - roman[s[i]]
                i += 2
                j += 2

            else:
                res += roman[s[i]]
                i += 1
                j += 1
        if i < n:
            return res + roman[s[i]]
        else:
            return res



s = Solution()
res = s.romanToInt("III")
print(res)
res = s.romanToInt("IV")
print(res)
res = s.romanToInt("IVIVI")
print(res)
res = s.romanToInt("IX")
print(res)
res = s.romanToInt("LVIII")
print(res)
res = s.romanToInt("MCMXCIV")
print(res)



