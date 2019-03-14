#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    a = int(line[1])
    line = sys.stdin.readline().strip()
    ori = list(map(lambda i: int(i), line.split()))
    values = list(map(lambda i: abs(int(i)-a), line.split()))
    res = 0
    # while len(values) > 1:
    idiot = min(values)
    res += idiot
    i = values.index(idiot)
    if i == len(values)-1:
        while len(ori) > 1:
            elem = ori.pop()
            res += abs(ori[-1] - elem)
            # elem = ori.pop()
            # values = list(map(lambda i: abs(i - elem), ori))
        print(res)
    elif i == 0:

        while len(ori) > 1:
            elem = ori[0]
            del ori[0]
            res += abs(elem - ori[0])
            ori.pop()
        print(res)
    else:
        pass
    # if i == len(values)-1:
    #     elem = ori.pop()
    #     values = list(map(lambda i: abs(i-elem), ori))
    #     while len(ori) > 1:
    #         res += values.pop()
    #         elem = ori.pop()
    #         values = list(map(lambda i: abs(i - elem), ori))
    #     print(res)
    # elif i == 0:
    #     elem = ori[0]
    #     values = list(map(lambda i: abs(i - elem), ori))
    #     del ori[0]
    #     del values[0]
    #     while len(ori) > 1:
    #         res += ori[0]
    #         ori.pop()
    #     print(res)
    # else:
    #     pass







    # print(ans)