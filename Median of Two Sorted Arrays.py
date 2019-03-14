class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        res = self.merge(nums1, nums2)
        if len(res) % 2 == 1:
            return float(res[int(len(res)/2)])
        else:
            return (res[int(len(res)/2)] + res[int(len(res)/2)-1])/2

    def merge(self, l1, l2):
        res = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        if i < len(l1):
            res.extend(l1[i:])
            # i = len(l1)
        elif j < len(l2):
            res.extend(l2[j:])
        else:
            return res
        return res






s = Solution()
res = s.findMedianSortedArrays([1, 3],[2])
print(res)

res = s.findMedianSortedArrays([1, 2],[3, 4])
print(res)
