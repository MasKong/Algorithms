class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """DFS"""
        l = []
        r_l = []
        candidates.sort()
        if candidates[0] > target:
            return []
        for i in candidates:
            if i == target:
                l.append([i])
            elif i < target:
                r_l.append([i])
        while len(r_l) != 0:
            current = r_l.pop()
            for item in candidates:
                if sum(current)+item == target:
                    idiot = list(current)
                    idiot.append(item)
                    idiot.sort()
                    if idiot not in l:
                        l.append(idiot)
                        break
                elif sum(current)+item > target:
                    break
                else:
                    idiot = list(current)
                    idiot.append(item)
                    r_l.append(idiot)

        return l


s = Solution()
result1 = s.combinationSum([2,3,6,7], 7)
result2 = s.combinationSum([2,3,5], 8)
# result3 = s.findPairs([1, 3, 1, 5, 4], k = 0)
# result4 = s.findPairs([1,1,1,1,1], k = 0)
print(result1)
# print(set(result1))
print(result2)
# print(result3)
# print(result4)

