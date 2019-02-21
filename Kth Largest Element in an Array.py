class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def divide(s, loc):
            if loc < 0 or loc >= len(s):
                raise IndexError
            div = s[loc]
            smaller = []
            greater = []
            for i in range(len(s)):
                if i == loc:
                    continue
                if s[i] <= div:
                    smaller.append(s[i])
                else:
                    greater.append(s[i])
            # smaller.append(div)
            return greater

        res = divide(nums,0)
        old_res = nums
        while len(res) > 1:
            if len(res) == k:
                res.sort()
                return res[0]

            if len(res) > k:
                old_res = res
                res = divide(res, 0)

            if len(res) < k:
                old_res.sort()
                return old_res[-k]

        old_res.sort()
        return old_res[-k]


s = Solution()
res = s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(res)
res1 = s.findKthLargest([3,2,1,5,6,4], 2)
print(res1)

