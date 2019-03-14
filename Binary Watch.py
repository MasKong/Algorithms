class Solution:
    def readBinaryWatch(self, num: 'int'):
        if num == 0:
            return '00:00'
        import itertools
        res = []
        for i in range(0, max(num, 4)):
            if i == 0:
                hours = ['0']
            else:
                hours = set(itertools.combinations('1111', i))
            if num-i == 0:
                minutes = ['0']
            else:
                minutes = set(itertools.combinations('111111', num-i))
            res.extend(self.combine(hours, minutes))


    def combine(self, l1, l2):
        print(l1)
        print(l2)
        res = []
        for i in l1:
            for j in l2:
                k = int(j, 2)
                if k <= 60:
                    res.append('{0}:{1}'.format(int(i, 2), k))



        return res


s = Solution()
res = s.readBinaryWatch(1)
print(res)
