class Solution:
    def heapsort(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def heapify(arr, n, i):
            """
            :type arr: List[int]
            :type n: int, length of arr
            :i: heaplify subtree rooted at i
            """
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[i] < arr[l]:
                largest = l

            if r < n and arr[largest] < arr[r]:
                largest = r

            if largest != i:
                arr[largest], arr[i] = arr[i], arr[largest]
                heapify(arr, n, largest)
            return arr

        arr = nums
        n = len(arr)

        # Build a maxheap.
        for i in range(n, -1, -1):
            heapify(arr, n, i)

            # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            heapify(arr, i, 0)
        return arr






s = Solution()
res = s.heapsort([3,2,3,1,2,4,5,5,6,0])
print(res)
res1 = s.heapsort([3,2,1,5,6,4])
print(res1)

