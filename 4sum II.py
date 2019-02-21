class Solution:
    def nSum(self, n, nums, target):
        if len(nums) < n:
            return []
        nums.sort()
        l_re = []
        def recursion_sum(n, nums, target, record):
            if sum(nums[:n]) > target or sum(nums[-n:]) < target:
                return #False
            if n == 2:
                '''two sum'''
                l, r = 0, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == target:
                        idiot = record[:]
                        idiot.extend([nums[l], nums[r]])
                        l_re.append(idiot)
                        # l_re.append(l_re + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
                # for i in range(len(nums)-1):
                #     if i > 0 and nums[i] == nums[i - 1]:
                #         continue
                #     for j in range(i+1,len(nums)):
                #         if j > i+1 and nums[j] == nums[j - 1]:
                #             continue
                #         # print(len(nums))
                #         # print(i,j)
                #         if nums[i] + nums[j] == target:
                #             idiot = record[:]
                #             idiot.extend([nums[i], nums[j]])
                #             l.append(idiot)



            else:
                for i in range(len(nums) - n + 1):
                    # if not record:
                    #     record = [nums[i]]
                    # else:
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    idiot = record[:]
                    idiot.append(nums[i])
                    # if n-1 < 2:
                    #     return
                    recursion_sum(n - 1, nums[i + 1:], target - nums[i], idiot)
                    # if n - 1 == 2:
                    #     break
                        #return



        '''main loop'''
        for i in range(len(nums)-n+1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            record = [nums[i]]
            recursion_sum(n-1, nums[i+1:], target-nums[i], list(record))
        # recursion_sum(n, nums, target, [])
        return l_re




    def fourSumCount(self, A, B, C, D):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.nSum(4, nums, target)

        # if len(nums) < 4:
        #     return []
        # nums.sort()
        # n = len(nums)
        # l = []
        # # print(nums)
        # if sum(nums[-4:]) < target:
        #     return []
        # for a in range(n-4+1):
        #     if sum([nums[a], nums[a+1], nums[a+2], nums[a+3]]) > target:
        #         break
        #     for b in range(a+1,n-3+1):
        #         if sum([nums[a], nums[b], nums[b + 1], nums[a + 2]]) > target:
        #             break
        #         for c in range(b+1,n-2+1):
        #             if sum([nums[a], nums[b], nums[c], nums[c + 1]]) > target:
        #                 break
        #             for d in range(c+1,n):
        #                 tar_l = [nums[a], nums[b], nums[c], nums[d]]
        #                 if sum(tar_l) == target:
        #                     if tar_l not in l:
        #                         l.append(tar_l)
        #                     break
        #                 elif sum(tar_l) > target:
        #                     break
        #
        # return l

s = Solution()

# nums = [1, 0, -1, 0, -2, 2]
# nums = [-3,-1,0,2,4,5]
nums1 = [0, 0, 0, 0]
nums = [-3,-2,-1,0,0,1,2,3]

target = 0
leg = s.fourSum(nums,target)
leg1 = s.fourSum(nums1, target)
print(leg)
print(leg1)