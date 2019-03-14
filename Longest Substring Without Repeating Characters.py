class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        i = 0
        j = 1
        # longest = 1
        res = 1
        while j < len(s):
            if s[j] in s[i:j]:
                i = s[i:j].find(s[j])+i+1
            elif j-i+1 > res:
                res = j-i+1
            j += 1
        return res




s = Solution()
res = s.lengthOfLongestSubstring("pwwkew")
print(res)
res = s.lengthOfLongestSubstring("abcabcbb")
print(res)
res = s.lengthOfLongestSubstring("bbbb")
print(res)
res = s.lengthOfLongestSubstring("bbtablud")
print(res)

