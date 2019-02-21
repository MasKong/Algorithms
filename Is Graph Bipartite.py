class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

s = Solution()

re1 = s.isBipartite([[1,3], [0,2], [1,3], [0,2]])
print(re1)

re2 = s.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]])
print(re2)


