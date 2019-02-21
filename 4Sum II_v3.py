class Solution:

    def fourSumCount(self, A, B, C, D):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        count = 0
        dic = {}
        for a in A:
            for b in B:
                result = a+b
                if result in dic:
                    dic[result] += 1
                else:
                    dic[result] = 1
        for c in C:
            for d in D:
                result = -c-d
                if result in dic:
                    count += dic[result]


        return count

s = Solution()
A = [1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
result1 = s.fourSumCount(A, B, C, D)
print(result1)
result2 = s.fourSumCount(*[[0,1,-1],
[-1,1,0],
[0,0,1],
[-1,1,1]])
print(result2)

result3 = s.fourSumCount(*[[-1,1,1,1,-1],
[0,-1,-1,0,1],
[-1,-1,1,-1,-1],
[0,1,0,-1,-1]])
print(result3)


