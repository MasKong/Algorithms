class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """BFS"""
        l = []
        candidates.sort()
        if candidates[0] > target:
            return []

        def dfs_recursion(candidates, target, stack):
            for item in candidates:
                if item > target:
                    return
                elif item == target:
                    l.append(list(stack))
                    l[-1].append(item)
                    return
                else:
                    idiot = list(stack)
                    idiot.append(item)
                    dfs_recursion(candidates[candidates.index(item):], target-item, list(idiot))
        dfs_recursion(candidates, target, [])
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

