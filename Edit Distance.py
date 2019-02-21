class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)+1    #row of matrix
        m = len(word2)+1    #column of matrix
        l = [n*[0] for i in range(m)]

        for i in range(m):
            l[i][0] = i
        for i in range(n):
            l[0][i] = i
        # print(l)
        for i in range(1,m):
            for j in range(1,n):
                # print(i,j)
                l[i][j] = min(l[i-1][j]+1, l[i][j-1]+1, l[i-1][j-1]+(word1[j-1]!=word2[i-1]))
        # l = [list(range(n)) for i in range(m)]
        print(l)
        return l[-1][-1]


s = Solution()
# word1 = "intention"
# word2 = "execution"
word1 = "horse"
word2 = "ros"
leg = s.minDistance(word1,word2)
print(leg)



