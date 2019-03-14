class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """BFS"""
        l = []
        r_l = []
        candidates.sort()
        if candidates[0] > target:
            return []
        # for i in range(len(candidates)):
        for i in candidates:
            if i == target:
                l.append([i])
            elif i < target:
                r_l.append([i]) #* len(candidates)
        while len(r_l) != 0:
            # record = list(range(len(r_l)))
            record = len(r_l)
            for i in range(len(r_l)):
                # if sum(r_l[i] > target):
                #     del
                for j in range(len(candidates)):
                    if sum(r_l[i])+candidates[j] > target:
                        break
                    else:
                        if sum(r_l[i])+candidates[j] == target:
                            r_l[i].append(candidates[j])
                            r_l[i].sort()
                            if r_l[i] not in l:
                                l.append(r_l[i])
                            break
                            # del r_l[i]
                        else:
                            new_l = list(r_l[i])
                            new_l.append(candidates[j])
                            r_l.append(new_l)
            r_l = r_l[record:]
        return l

        # l = []
        # candidates.sort()
        # if candidates[0] > target:
        #     return []
        # for i in range(len(candidates)):
        #     if candidates[i] > target:
        #         break
        #     if candidates[i] == target:
        #         l.append(candidates[i])
        #     else:
        #         result = self.combinationSum(candidates, target-candidates[i])
        #         if len(result) != 0:
        #             l.append([candidates[i]].extend(result))
        #
        # return l


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

