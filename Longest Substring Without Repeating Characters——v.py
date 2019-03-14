class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        l = []
        # j = 0
        # find the longest substring of the initial character
        for i in range(1, len(s)):
            if s[i] in s[:i]:
                l.append(i)
                break
        if len(l) == 0:
            l.append(len(s))

        '''Dynamic Programming'''
        for i in range(1, len(s)):
            j = min(l[-1] - 1,1)    #the position of the repeated char
            if j + i >= len(s):     # the repeat char is the last char in the string
                l.append(j)
            for t in range(j + i, len(s)):  #eliminate the repeated char
                if s[t] in s[i:t]:
                    l.append(t - i)
                    break
            if len(l) != i+1:   #substring without repeating from start position i
                l.append(len(s)-i)
        return max(l)

s = Solution()
res = s.lengthOfLongestSubstring("pwwkew")
print(res)
res = s.lengthOfLongestSubstring("abcabcbb")
print(res)
res = s.lengthOfLongestSubstring("bbbb")
print(res)
res = s.lengthOfLongestSubstring("bbtablud")
print(res)