def compute_prefix(p):
    l = [0] * len(p)
    k = 0
    for i in range(1,len(p)):
        '''#This line decrease k. because 0 < k < i, the total time that i has been increased < len(p),
        so the total time that while loop execute would < len(p)'''
        while k>0 and p[i] != p[k]:
            '''judge whether the chars of new positions equal'''
            k = l[k]
        if p[i] == p[k]:
            k += 1                          # this increase k
        l[i] = k
    return l

def KMP_Match(s,p):
    '''print the matched string'''
    if not p:
        return None
    record = [] #record the length of matched string
    l = compute_prefix(p)
    # print(l)
    q = 0
    for i in range(0,len(s)):
        while q > 0 and p[q] != s[i]:
            '''judge whether the chars of new positions equal'''
            record.append(q)
            q = l[q]
        if p[q] == s[i]:
            q += 1
        if q == len(p):
            record.append(q)
            print(s[i-q+1:i+1])
            q = l[q-1]
    return record



s = "abaabcac"
print (compute_prefix(s))
print(KMP_Match("zw12abc", "12abc"))
print(KMP_Match("zw12abc", ""))
print(KMP_Match("zw12abcddabc", "abc"))


class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in S
        """
        partial, ret, j = self.partial(P), [], 0

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P):
                ret.append(i - (j - 1))
                j = 0


k = KMP()
print(k.partial("abaabcac"))

