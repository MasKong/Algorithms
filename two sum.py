class Solution:
    def twoSum(self, nums, target: int):
        if len(nums) < 2:
            return []
        if len(nums) == 2:
            return [0,1]
        d = {}
        for i in range(len(nums)):
            if nums[i] in d.keys():
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        # print(d)
        for i in range(len(nums)):
            if target-nums[i] in d.keys():
                if len(d[target-nums[i]]) == 1 and d[target-nums[i]][0] != i:
                    return [i,d[target-nums[i]][0]]
                elif len(d[target-nums[i]]) == 2:
                    return d[target-nums[i]]


s = Solution()
res = s.twoSum([3,2,4], 6)
print(res)

