# divide and conquer
#recursively divide a problem into subproblems. O(nlogn)

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        right = len(nums)-1     #index of the last item
        # if right == 0:
        #     return None
        if right == left:     #only one element
            return nums[0]
        mid = int(len(nums) / 2)
        # print("mid",mid, left, right)
        # print(self.max_cross(nums),
        #       self.maxSubArray(nums[left:mid]), self.maxSubArray(nums[mid:right]),)
        m = self.max_cross(nums)
        l = self.maxSubArray(nums[left:mid])
        r = self.maxSubArray(nums[mid:right+1])
        return max(m,l,r)
        # return r

    def max_cross(self, nums):
        mid = int(len(nums)/2)
        left = 0
        right = len(nums)-1
        left_sum_max, right_sum_max = float("-inf"), float("-inf")
        left_sum, right_sum = 0,0
        left_index, right_index = -1,-1
        for i in range(mid-1,left-1,-1):
            left_sum += nums[i]
            if left_sum>left_sum_max:
                left_index = i
                left_sum_max = left_sum
        for i in range(mid,right+1):
            right_sum += nums[i]
            if right_sum>right_sum_max:
                right_index = i
                right_sum_max = right_sum
        return left_sum_max+right_sum_max
s = Solution()
leg = s.maxSubArray([-1,2,3,-6,8])
# leg = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# leg = s.max_cross([-2,1,-3,4,-1,2,1,-5,4])

print(leg)