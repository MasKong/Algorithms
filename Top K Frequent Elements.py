class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        d = {}
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        l = []
        for i in d.keys():
            l.append((i, d[i]))
        l = list(map(lambda i: i[0], sorted(l, key=lambda i:i[1])[len(l)-k:]))
        # l = l
        # l = tuple(d)
        # l.sort()
        return l



s = Solution()
res = s.topKFrequent(nums=[1,1,1,2,2,3], k = 2)
print(res)
