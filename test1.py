#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys
for line in sys.stdin:
    l = list(map(lambda i: ord(i), line.strip().lower()))
    i = 0
    n = len(l)
    while i < n-1:
        if l[i] > l[i+1] and l[i] in l[i+2:]:
            del l[i]
            n = len(l)
        else:
            i += 1
    print(chr(l[0]))












