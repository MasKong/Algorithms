def f(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        if l[0] == 0:
            return 1
        else:
            return 0
    # res = [l[0]]
    res = 0
    idiot = sum(l[1:])
    n = len(l)
    for i in range(0, n-1):
        if l[i] == -idiot:
            inter = n-i
            if inter > res:
                res = inter
        else:
            idiot -= l[i+1]
    return res

res = f([1,1,-1,1,-1])
print(res)
res = f([0])
print(res)
res = f([-1])
print(res)
res = f([-1,1])
print(res)
res = f([-1,1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1])
print(res)
# res = f(-1,4,15)
# print(res)
# res = f(0,-1,5)
# print(res)


