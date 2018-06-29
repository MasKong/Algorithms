class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        l = 0
        r = len(s)-1
        # print(s[:r]+(s[r+1:]))
        # print(s[r+1:])
        while l < r:
        # for i in range(len(a)):
            if s[l]!= s[r]:
                return max(self.non_recur_isPalindrome(s[:l]+(s[l + 1:])),
                    self.non_recur_isPalindrome(s[:r]+(s[r + 1:])))
                # return max(self.isPalindrome(s[:l].join(s[l+1:])),self.isPalindrome(s[:r].join(s[r+1:])))
            l+=1
            r-=1
        return True

    def non_recur_isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        l = 0
        r = len(s)-1
        while l < r:
        # for i in range(len(a)):
            if s[l]!= s[r]:
                return False
            l+=1
            r-=1
        return True
s = Solution()

leg = s.isPalindrome("abcd")
print(leg)