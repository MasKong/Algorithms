class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # t = s.lower()
        # t_re = t[::-1]
        # c_t = 0
        # c_re = 0
        # for i in range(int(len(t)/2)):
        #
        # a = sorted(t)
        # b = sorted(t_re)
        if len(s) == 0:
            return True
        l = 0
        r = len(s)-1
        while l < r:
        # for i in range(len(a)):
            while l <r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
s = Solution()
# leg = s.maxSubArray([-1,2,3,-6,8])

# leg = s.max_cross([-2,1,-3,4,-1,2,1,-5,4])
# a = "anagram"
# b = "nagaram"
# a = "aacc"
# b = "accc"
leg = s.isPalindrome("A man, a plan, a canal: Panama")
print(leg)