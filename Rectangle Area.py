class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        overlap = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
        return (A - C) * (B - D) + (E - G) * (F - H) - overlap
    # def computeArea(self, A, B, C, D, E, F, G, H):
    #     """
    #     :type A: int
    #     :type B: int
    #     :type C: int
    #     :type D: int
    #     :type E: int
    #     :type F: int
    #     :type G: int
    #     :type H: int
    #     :rtype: int
    #     """
    #     s1 = abs(A-C) * abs(B-D)
    #     s2 = abs(E-G) * abs(F-H)
    #     cross = self.find_cross(A, B, C, D, E, F, G, H)
    #     return s2+s1-cross
    #
    # def find_cross(self,A, B, C, D, E, F, G, H):
    #     # leftx1 = min(A,C)    #left border
    #     # leftx2 = max(A,C)    #right border
    #     # rightx1 = min(E,G)
    #     # rightx2 = max(E, G)
    #     # lefty1 = min(B,D)    #left border
    #     # lefty2 = max(B,D)    #right border
    #     # righty1 = min(F,H)
    #     # righty2 = max(F,H)
    #     A1 = (A,D)
    #     B1 = (A,B)
    #     C1 = (C,D)
    #     D1 = (C,B)
    #     A2 = (E,H)
    #     B2 = (E,F)
    #     C2 = (G,H)
    #     D2 = (G,F)
    #     '''NO points in another square'''
    #
    #     if A2[0]>=A and A2[0]<=C:
    #         if
    #     cross = (righty2- lefty1) * (leftx2-rightx1)
    #     print(cross)
    #     return cross
    #     # if E >= A:
    #     #     left =
    #     # if E >= A and E <= C and H >= B and H <= D:
    #     #     return (E-C) *
    #     # else:
    #     #     return 0

s = Solution()
# leg = s.maxSubArray([-1,2,3,-6,8])

# leg = s.max_cross([-2,1,-3,4,-1,2,1,-5,4])
# a = "anagram"
# b = "nagaram"
# a = "aacc"
# b = "accc"
leg = s.computeArea(A = -3, B = 0, C = 3, D = 4, E = -13, F = -1, G = 9, H = 4)
# leg = s.computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2)
print(leg)