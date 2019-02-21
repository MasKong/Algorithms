class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def twosum(nums, target):   #assume nums is sorted
            assert not len(nums) >= 2, "length has to be greater than or equal to 2"
            i, j = 0, len(nums)-1
            while i < j:
                temp_result = nums[i] + nums[j]
                if temp_result < target:
                    i += 1
                elif temp_result > target:
                    j -= 1
                else:
                    return True

        def twosum_closest(nums, target):   #assume nums is sorted
            assert len(nums) >= 2, "length has to be greater than or equal to 2"
            i, j = 0, len(nums)-1
            cloest = float("inf")
            while i < j:
                temp_result = nums[i] + nums[j]
                if temp_result < target:
                    i += 1
                elif temp_result > target:
                    j -= 1
                else:
                    return True
                if abs(temp_result - target) < cloest:
                    cloest = abs(temp_result - target)

            return cloest + target


        # nums.sort()
        # cloest = float("inf")
        # for i in range(len(nums)-2):
        #     result = twosum_closest(nums[i+1:], target-nums[i])
        #     if isinstance(result, bool):
        #         return target
        #     else:
        #         temp = abs(result + nums[i] - target)
        #         if temp < cloest:
        #             cloest = temp
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                s = sum((nums[i], nums[j], nums[k]))
                if abs(s-target) < abs(closest-target):
                    closest = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return s
        return closest




s = Solution()
# re1 = s.threeSumClosest([-1, 2, 1, -4], 1)
# print(re1)

re2 = s.threeSumClosest([0,0,0], 1)
print(re2)


