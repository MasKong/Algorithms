# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         if dividend == 0:
#             return 0
#         if dividend > 0 and divisor > 0 or (dividend<0 and divisor<0):
#             sign = 1
#         else:
#             sign = -1
#         if divisor == 1:
#             if dividend >= 2147483648:
#                 return 2147483647
#             else:
#                 return dividend
#         elif divisor == -1:
#             if -dividend < -2147483648:
#                 return -2147483648
#             elif -dividend >= 2147483648:
#                 return 2147483647
#
#             else:
#                 return -dividend
#         dividend = abs(dividend)
#         divisor = abs(divisor)
#         count = 0
#         while dividend > 0:
#             dividend -= divisor
#             count += 1
#         if dividend < 0:
#             count -= 1
#         if sign == 1:
#             return count
#         else:
#             return -count
class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

s = Solution()
res = s.divide(-2147483648, -1)
print(res)
s = Solution()
res = s.divide(1, 1)
print(res)
s = Solution()
res = s.divide(3, 10)
print(res)
s = Solution()
res = s.divide(10, 3)
print(res)
s = Solution()
res = s.divide(7, -3)
print(res)