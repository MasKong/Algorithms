class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        sum_record = 0
        pointer = 0
        result = len(nums)
        for i in range(len(nums)):
            sum_record += nums[i]
            while sum_record >= s:
                temp = i - pointer + 1
                if temp < result:
                    result = temp

                sum_record -= nums[pointer]
                pointer += 1

        return result




s = Solution()
re1 = s.minSubArrayLen(7, [2,3,1,2,4,3])
print(re1)



