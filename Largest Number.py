class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(lambda i:str(i), nums))

        nums = sorted(nums, key=lambda i:i[0])
        # nums = sorted(nums, key=len)
        return nums


s = Solution()
res = s.largestNumber([9,90])
print(res)

res1 = s.largestNumber([90,1,11,12,9,999])
print(res1)
