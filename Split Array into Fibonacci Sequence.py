class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        if len(S) < 3:
            return []
        if S[0] == 0:
            return []
        # l = []
        # i = 1
        # j = 1
        # k = 1

        # if len(l) == 0:
        #     return []
        r = self.find_element(S)
        if r is None:
            return []
        else:
            l,a,b,c = r[0], r[1], r[2], r[3]
        count = a+b+c
        f = 0
        while count+c <= len(S):
            if l[-1] + l[-2] == int(S[count:count+c]):
                l.append(int(S[count:count+c]))
                count += c
                f = 0
            else:
                c+=1
                f = 1
        if f == 1:
            return []
        else:
            return l

    def find_element(self,S):
        l = []
        for i in range(1,int(len(S)/2-1)):

            for j in range(1,int(len(S)/2-1)):

                for k in range(max(i,j),len(S)-i-j+1):
                    if int(S[0:i]) + int(S[i:j+i]) == int(S[j+i:j+i+k]):
                        # a = i
                        # b = j
                        # c = k
                        l.append(int(S[0:i]))
                        l.append(int(S[i:j+i]))
                        l.append(int(S[j+i:j+i+k]))
                        return((l,i,j,k))
        return None


s = Solution()
leg = s.splitIntoFibonacci('123456579')
# leg = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# leg = s.max_cross([-2,1,-3,4,-1,2,1,-5,4])

print(leg)



