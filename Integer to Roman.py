class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        roman_v = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90:'XC',
                   50: 'L', 40:'XL', 10: 'X', 9:'IX', 5: 'V', 4:'IV', 1: 'I'}
        if num == 0:
            return ""
        # print(roman.values())
        res = ""
        for k in roman_v.keys():
            c = int(num / k)
            if c != 0:
                res += roman_v[k] * c

                num -= c * k
        return res


s = Solution()
res = s.intToRoman(3)
print(res)
s = Solution()
res = s.intToRoman(4)
print(res)
s = Solution()
res = s.intToRoman(9)
print(res)
s = Solution()
res = s.intToRoman(58)
print(res)
s = Solution()
res = s.intToRoman(1994)
print(res)