# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         i = 0
#         j = 0
#         n = len(s)
#         m = len(p)
#         if n == 0 and m == 0:
#             return True
#         if n > 0 and m == 0:
#             return False
#         if n == 0 and m < 2:
#             return False
#         if n == 0 and m > 1:
#             if p[1] != '*':
#                 return False
#             else:
#                 return self.isMatch("", p[2:])
#         while i < n:
#             if s[i] == p[j]:
#                 if j < m-1 and p[j+1] != '*':
#                     i += 1
#                     j += 1
#                 elif j < m-1 and p[j+1] == '*':
#                     while s[i] == p[j]:
#                         i += 1
#                         if i >= n:
#                             break
#                     j += 2
#                 else:   #the two last elements are the same
#                     if i == n-1:
#                         return True
#                     else:   #pattern string is done
#                         return False
#             elif p[j] == '.':
#                 if j < m-1 and p[j+1] != '*':
#                     i += 1
#                     j += 1
#                 elif j < m - 1 and p[j + 1] == '*':
#                     if j + 2 < m-1:
#                         return self.isMatch("", p[j+2:])
#                     else:
#                         return True
#                 else:   #j == m-1
#                     j += 1
#                     i += 1
#                     if i < n:
#                         return False
#                     elif i == n:
#                         return True
#             elif j < m-1 and p[j+1] == '*':
#                 j += 2
#                 if j >= m:
#                     return False
#
#             else:
#                 return False
#
#         if j < m:
#             return self.isMatch("", p[j:])
#         elif j == m:
#             return True

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in ['.', s[0]]
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    (first_match and self.isMatch(s[1:], p)))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


s = Solution()
res = s.isMatch("ab", ".*c")
print(res)
s = Solution()
res = s.isMatch("b", ".*c")
print(res)
s = Solution()
res = s.isMatch("", ".*c")
print(res)
s = Solution()
res = s.isMatch("b", "*c")
print(res)
s = Solution()
res = s.isMatch("b", "c")
print(res)
s = Solution()
res = s.isMatch("b", "c")
print(res)
s = Solution()
res = s.isMatch("bbab", "b*a*")
print(res)
s = Solution()
res = s.isMatch("a", "")
print(res)
s = Solution()
res = s.isMatch("abcd", "d*")
print(res)
s = Solution()
res = s.isMatch("aa", "a")
print(res)
s = Solution()
res = s.isMatch("aa", "a*")
print(res)
s = Solution()
res = s.isMatch("ab", ".*")
print(res)
s = Solution()
res = s.isMatch("aab", "c*a*b")
print(res)
s = Solution()
res = s.isMatch("mississippi", "mis*is*p*.")
print(res)





