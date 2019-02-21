'''find subsequence'''
def subseq(w1, w2):
    i = 0
    for c in w2:
        if i < len(w1) and w1[i] == c :
            i += 1
    # print(i)
    return i == len(w1)

a = 'aa'
b = 'aaaaa'
re = subseq(a,b)
print(re)



