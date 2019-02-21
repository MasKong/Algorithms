# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    s = A
    res = sum(s)
    can = s[1:-1]
    can.sort()
    for i in range(len(can)-1):
        if i > 0 and s[i] == s[i-1]:
            continue
        for j in range(i+1,len(can)):
            if j > i+1 and can[j] == can[j-1]:
                continue
            if (res - s[i] - s[j]) % 3 == 0:
                return True

    return False



s = solution([1,3,4,2,2,2,1,1,2])
print(s)

print(solution([1,1,1,1,1,1]))

print(solution([1,1,1,1,1]))

print(solution([1,1,1,1,1,1]))

print(solution([1,2]*10000))




