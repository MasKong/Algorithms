class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


        def partition(nums, k=-1):
            # ind = nums[-1]
            i = -1
            for j in range(0, len(nums)-1):
                nums[k], nums[-1] = nums[-1], nums[k]
                if nums[j] < nums[-1]:
                    i = i + 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[-1], nums[i+1] = nums[i+1], nums[-1]
            return i+1

        if len(nums) < k:
            return []
        # k = k - 1  # in python, the index starts from 0
        ind = partition(nums)
        # print(ind)
        if ind < k-1:
            return self.findKthLargest(nums[ind+1:], k-ind-1)
        elif ind > k-1:
            return self.findKthLargest(nums[:ind], k)
        else:
            return nums[k-1]




s = Solution()
res = s.findKthLargest([3,2,3,], 4)
print(res)
res = s.findKthLargest([1,2,3,4], 4)
print(res)
res = s.findKthLargest([1,2,3,4,5,6], 2)
print(res)
res = s.findKthLargest([1,2,3,4,5,6], 5)
print(res)
res = s.findKthLargest([3,2,3,1,2,4,5,5,6,0], 7)
print(res)
res1 = s.findKthLargest([3,2,1,5,6,4], 3)
print(res1)

