def quick_sort(a):
    # if len(a) < 1:
    #     return
    # if len(a) == 1:
    #     return a
    if len(a) > 1:
    # if n >= 1:
        '''choose the last element as pivot'''
        def partition(a):
            j = -1
            for i in range(0, len(a)):
                if a[i] < a[-1]:
                    j += 1
                    a[j], a[i] = a[i], a[j]
            # print(a)
            a[-1], a[j+1] = a[j+1], a[-1]
            return j+1

        r = partition(a)
        # print(r)
        # if r == 0 or r == len(a)-1:
        #     return a
        a[:r - 1] = quick_sort(a[:r - 1])
        a[r + 1:] = quick_sort(a[r + 1:])

        # a[:r] = quick_sort(a[:r-1])
        # a[r:] = quick_sort(a[r+1:])
    return a


# def quick_sort(array, l, r):
#     if l < r:
#         q = partition(array, l, r)
#         print(q)
#         quick_sort(array, l, q - 1)
#         quick_sort(array, q + 1, r)
#     return array
#
#
# def partition(array, l, r):
#     x = array[r]
#     i = l - 1
#     for j in range(l, r):
#         if array[j] <= x:
#             i += 1
#             array[i], array[j] = array[j], array[i]
#     array[i + 1], array[r] = array[r], array[i + 1]
#     return i + 1




res = quick_sort([3,2,3,1,2,4,5,5,6])
# a = [1,3,2,4,7]
# res = quick_sort([1,3,2,4,7])
# res = quick_sort([1,3,2,4,7],0,4)
print(res)

