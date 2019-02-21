class Solution:
    def subseq(self, w1, w2):
        # True iff word1 is a subsequence of word2.
        i = 0
        for c in w2:
            if i < len(w1) and w1[i] == c:
                i += 1
        return i == len(w1)

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        if not strs:
            return 0
        l = sorted(strs, key=len)
        # print(l)
        for i in range(len(l)-1, -1, -1):
            flag = 1
            temp = l[:]
            del temp[i]
            for item in temp:
                if self.subseq(l[i], item):
                    flag = 0
                    break
            if flag == 1:
                return len(l[i])


        return -1




s = Solution()
re = s.findLUSlength(["aba", "cdc", "eae"])
print(re)

re1 = s.findLUSlength(["aaa","aaa","aa"])
print(re1)


