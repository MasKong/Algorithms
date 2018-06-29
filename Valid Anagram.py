class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1=[]
        l2=[]
        if len(t) != len(s):
            return False
        for i in t:
            l1.append(ord(i))
        for j in s:
            l2.append(ord(j))
        l1.sort()
        l2.sort()
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True


s = Solution()
# leg = s.maxSubArray([-1,2,3,-6,8])

# leg = s.max_cross([-2,1,-3,4,-1,2,1,-5,4])
# a = "anagram"
# b = "nagaram"
a = "aacc"
b = "accc"
leg = s.isAnagram(a,b)
print(leg)