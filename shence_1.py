def f(x, y, m):
    if max(x,y) < m and x <= 0 and y <= 0:
        return -1
    # if x+y > m:
    #     return 0
    l = [min(x,y), max(x,y)]
    count = 0
    while l[1] < m:
        idiot = l[0] + l[1]
        if idiot > l[1]:
            l[0], l[1] = l[1], idiot
        else:
            l[0] = idiot
        count += 1
    return count

res = f(1,2,2**32)
print(res)
res = f(-1,4,15)
print(res)
res = f(0,-1,5)
print(res)


