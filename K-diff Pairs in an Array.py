class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[j] - nums[i] == k:
                    count += 1
                elif nums[j] - nums[i] > k:
                    break
                # if j != len(nums)-1:
        return count




s = Solution()
result1 = s.findPairs([3, 1, 4, 1, 5], k = 2)
result2 = s.findPairs([1, 2, 3, 4, 5], k = 1)
result3 = s.findPairs([1, 3, 1, 5, 4], k = 0)
result4 = s.findPairs([1,1,1,1,1], k = 0)
print(result1)
print(result2)
print(result3)
print(result4)














