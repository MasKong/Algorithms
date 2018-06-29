#coding=utf-8
import sys
def maxSubArray(nums):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    if len(nums) == 1:
        return nums[0]
    l = [nums[0]]
    if nums[0] == 0:
        k = 1
    else:
        k = 0
    for i in range(1,len(nums)):
        # if nums[i] <0:
        if nums[i] == 0:
            k+=1
        if k > 3:
            l.append(0)
            k = 0
            continue
        if l[i-1] >0:
            l.append(nums[i] + l[i-1])
        else:
            l.append(nums[i])
    print(max(l))
    #return max(l)

if __name__ == "__main__":
        # 读取每一行
    line1 = sys.stdin.readline()

    para = list(map(int, line1.split()))
    n = para[0]
    m = para[1]
    l = []
    for i in range(n):
        l.append(int(sys.stdin.readline()))
    # l.sort()
    # l.reverse()
    s = 0
    for i in range(n-1):
        for j in range(i+1,n):
            ans= int(int(abs(l[i]-l[j]))/m)
            # print(ans)
            s += ans
    print(s)
    # values = list(map(int, line.split()))
    # ans = maxSubArray(values)
    #print(ans)