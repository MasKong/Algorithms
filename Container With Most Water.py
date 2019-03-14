class Solution:
    def maxArea(self, height: list) -> int:
        max_area = 0
        n = len(height)
        # for i in range(n-1):
        #     for j in range(1,n):
        i = 0
        j = n - 1
        while i < j:
            res = (j-i) * min(height[i], height[j])
            if res > max_area:
                max_area = res
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

s = Solution()
res = s.maxArea([1,8,6,2,5,4,8,3,7])
print(res)
s = Solution()
res = s.maxArea([1,2,1,1,2,1,])
print(res)
