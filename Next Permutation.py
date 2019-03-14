class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        # res = ""
        # c = 0
        # for i in range(n-1, 0, -1):
        #     # for j in range(i-1, -1, -1):
        #     #     if nums[i] > nums[j]:
        #     #         nums[i], nums[j] = nums[j], nums[i]
        #     #         return
        #     # res += str(nums[i])
        #     if nums[i] > nums[i-1]:
        #
        #         c = i-1
        #         break
        right = len(nums) - 1
        while nums[right] <= nums[right - 1] and right - 1 >= 0:
            right -= 1
        # if c == n-1:
        #     nums[-1], nums[-2] = nums[-2], nums[-1]
        #     return
        # print(c)
        # if c == 0:
        #     self.reverse(nums, 0, n-1)
        if right == 0:
            return self.reverse(nums, 0, len(nums) - 1)
        pivot = right - 1
        successor = 0
        # find rightmost succesor
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        # swap pivot and successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        # reverse suffix
        self.reverse(nums, pivot + 1, len(nums) - 1)
        # else:
        #     c -= 1
        #     for j in range(n-1, c, -1):
        #         if nums[j] > nums[c]:
        #             nums[j], nums[c] = nums[c], nums[j]
        #             break
        #
        # self.reverse(nums, c+1, n-1)
        # return

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # print(c)
        # if c == -1 and len(nums) == 0:
        #     return
        # else:
        #     nums =  nums[::-1]
        # if c == -1:
        #     return
        #
        # if c == n-1:
        #     nums[-1], nums[-2] = nums[-2], nums[-1]
        #     return


    # def nextPermutation(self, nums) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     res = ""
    #     c = -1
    #     for i in range(n-1, -1, -1):
    #         res += str(nums[i])
    #         if i > 0 and nums[i] < nums[i-1] and c<0:
    #             c = i
    #     print(c)
    #     if c != n-1:
    #         nums[-1], nums[-2] = nums[-2], nums[-1]
    #         return nums
    #     else:
    #         for j
    #     while c > 0:
    #         inter = res[:c-1] + str(nums[c]) + str(nums[c-1])
    #
    #         if int(inter) > int(res):
    #             nums[c], nums[c - 1] = nums[c - 1], nums[c]
    #             # return
    #             return nums     #for testing
    #         else:
    #             c -= 1
    #     if c == -1:
    #         if len(nums) > 1:
    #             nums[-1], nums[-2] = nums[-2], nums[-1]
    #     if c == 0:  #descending order
    #         for i in range(1,n-1):
    #             if nums[i] > nums[i+1]:
    #                 nums[i], nums[i+1] = nums[i+1], nums[i]
    #     return nums  # for testing




s = Solution()
l = [1,3,2]
s.nextPermutation(l)
print(l)
l = [2,1,3]
s.nextPermutation(l)
print(l)
l = [1,2,3]
s.nextPermutation(l)
print(l)
l = [3,2,1]
s.nextPermutation(l)
print(l)
l = [1,1,5]
s.nextPermutation(l)
print(l)
l = []
s.nextPermutation(l)
print(l)

