import numpy as np

class Edit_Distance:
    def __init__(self):
        self.back_trace = None
        self.n = 0
        self.m = 0
        self.l = None

    def insertion_cost(self,c1):
        '''customize your insertion cost'''
        return 1

    def deletion_cost(self,c1):
        '''customize your deletion cost'''
        return 1

    def substitution_cost(self,c1,c2):
        '''customize your substitution cost'''
        if c1 == c2:
            return 0
        return 2

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)+1    #row of matrix
        m = len(word2)+1    #column of matrix
        self.n = n
        self.m = m
        l = np.zeros((m,n))
        # back_trace = np.zeros((m,n))
        back_trace = [n*[0] for i in range(m)]

        for i in range(m):
            l[i,0] = i
        for i in range(n):
            l[0,i] = i
        # print(l)
        for i in range(1,m):
            for j in range(1,n):
                # print(i,j)
                cost = [l[i-1][j]+self.insertion_cost(word2[i-1]), l[i][j-1]+self.deletion_cost(word1[j-1]), l[i-1][j-1]+self.substitution_cost(word1[j-1],word2[i-1])]
                min_cost = min(cost)
                print((i,j),min_cost)
                back_trace[i][j] = [i for i,j in enumerate(cost) if j == min_cost]
                l[i][j] = min_cost
        # l = [list(range(n)) for i in range(m)]
        # print(l)
        # print(back_trace)
        self.l = l
        self.back_trace = back_trace
        return l[-1][-1]

    # def print_direction(self,l):
    #     if

    def output_back_trace(self):
        i = self.n-1
        j = self.m-1
        while i >= 0 and j >= 0:

            # print((i,j))
            direction_list = self.back_trace[i][j]   #choose the last direction, here every direction has the same cost
            print(direction_list)
            if isinstance(direction_list,list):
                direction = direction_list[0]
            else:
                direction = direction_list
            if direction == 2:
                i -= 1
                j -= 1
            elif direction == 1:
                j -= 1
            else:
                i -= 1
            # print(self.l[i][j])

s = Edit_Distance()
# word1 = "intention"
# word2 = "execution"
word1 = "execution"
word2 = "intention"
leg = s.minDistance(word1,word2)
print(leg)
s.output_back_trace()
print(s.l)





