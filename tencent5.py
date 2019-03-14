#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    # ans = 0
    if n == 0 and n == 1:
        print(None)
    # for i in range(n):
        # 读取每一行
    line = sys.stdin.readline().strip()
    # if n == 1:
    #     print()
        # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    # print(values)
    for i in range(1,n):
        pos = 1
        v = abs(values[i] - values[0])
        for j in range(0, i):
            inter = abs(values[i] - values[j])
            if inter < v:
                v = inter
                pos = j+1
        print("{} {}".format(v, pos))




    # print(ans)