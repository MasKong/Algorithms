class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = []
        a = {}      #store the count of each character for pattern string p
        b = {}
        for i in p:
            a[i] = p.count(i)
            b[i] = s[:len(p)].count(i)
        # for i in s[:len(p)]:
        #     b[i] =
        # print(b)
        if a == b:
            l.append(0)
        if len(s) == 0:
            return []
        for i in range(1,len(s)-len(p)+1):
            if s[i - 1] in a.keys():
                b[s[i - 1]] -= 1
            if s[i+len(p)-1] in a.keys():
                b[s[i + len(p) - 1]] += 1
            # try:
            #
            #     b[s[i - 1]] -= 1
            # except KeyError:
            #     continue
            #
            # try:
            #
            #     b[s[i+len(p)-1]] += 1
            # except KeyError:
            #     continue
            # print(a)
            # print(b)

            if b == a:
                l.append(i)
        return l



s = Solution()
# leg = s.maxSubArray([-1,2,3,-6,8])

# leg = s.max_cross([-2,1,-3,4,-1,2,1,-5,4])
# a = "anagram"
# b = "nagaram"
a = "baa"
b = "aa"
leg = s.findAnagrams(a,b)
print(leg)