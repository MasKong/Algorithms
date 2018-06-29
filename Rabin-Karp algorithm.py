'''please input pattern and string'''
p = input()
s = input()
d = int(input())
q = int(input())
l_p = len(p)
h = d**(l_p-1) % q
'''Preprocessing'''
p_sum, s_sum = 0,0
for i in range(0,l_p):
    p_sum = (d*p_sum + int(p[i])) %q
    s_sum = (d * s_sum + int(s[i])) %q
    # p_sum = (p_sum+(d*p_sum + int(p[i]))) % q
    # s_sum = (s_sum+(d * s_sum + int(s[i]))) % q

for j in range(0,len(s)-l_p+1):
    if p_sum == s_sum:
        if s[j:j+l_p] == p:
            print(s[j:j+l_p])
    if j < len(s)-l_p:
        s_sum = (d*(s_sum-int(s[j])*h) + int(s[j+l_p])) % q


