class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        i = 1
        j = 0
        n = len(nums)
        while i < n:
            # if nums[i] == nums[j]:
            #     continue
            if nums[i] > nums[j]:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

            i += 1
        return j+1


s = Solution()
res = s.removeDuplicates([1,1,2])
print(res)
s = Solution()
res = s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(res)
