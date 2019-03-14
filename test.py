#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print(0)
    ans = 0
    l = []
    for i in range(2):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        l.append(list(map(int, line.split())))
    l1 = l[0]
    l2 = l[1]
    l1.sort()
    l2.sort()
    l2 = l2[::-1]
    for i in range(n):
        ans += l1[i] * l2[i]
    print(ans)