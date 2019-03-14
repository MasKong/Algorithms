class Solution:

    def nSum(self, n, nums, target):
        [item.sort() for item in nums]
        l_re = []
        # print(nums)

        def early_termination(nums):
            if sum([item[-1] for item in nums]) < target or sum([item[0] for item in nums]) > target:
                return True


        def recursion_sum(n, nums, target):
            if early_termination(nums):
                return

            if n == 2:
                '''two sum'''
                l, r = 0, len(nums[-1]) - 1
                while l < len(nums[0]) and r >= 0:
                    if nums[0][l] + nums[1][r] == target:
                        l_re.append(1)
                        l_equal = 0
                        r_equal = 0
                        l += 1
                        r -= 1
                        while l < len(nums[0])-1 and nums[0][l] == nums[0][l-1]:
                            l_equal += 1
                            l += 1
                        while r > 0 and nums[1][r] == nums[1][r+1]:
                            r_equal += 1
                            r -= 1
                        if l_equal != 0 or r_equal != 0:
                            total_connect = (l_equal+1) * (r_equal+1) -1
                            print("equal", total_connect)
                            print("l_equal", l_equal)
                            print("r_equal", r_equal)
                            l_re.extend([1 for _ in range(total_connect)])

                    elif nums[0][l] + nums[1][r] < target:
                        l += 1
                    else:
                        r -= 1

            else:
                for i in range(len(nums[0])):
                    recursion_sum(n - 1, nums[1:], target - nums[0][i])

        '''main loop'''
        for i in range(len(nums[0])):
            recursion_sum(n - 1, nums[1:], target - nums[0][i])
        return len(l_re)

    def fourSumCount(self, A, B, C, D):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # print([A, B, C, D])
        return self.nSum(4, [A, B, C, D], 0)

s = Solution()
A = [1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
# result1 = s.fourSumCount(A, B, C, D)
# print(result1)
# result2 = s.fourSumCount(*[[0,1,-1],
# [-1,1,0],
# [0,0,1],
# [-1,1,1]])
# print(result2)

result3 = s.fourSumCount(*[
    [-1, -1, 1, 1, 1],
    [-1, -1, 0, 0, 1],
    [-1, -1, -1, -1, 1],
    [-1, -1, 0, 0, 1]])
print(result3)


