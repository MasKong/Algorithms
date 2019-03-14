# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     idiot = sys.stdin.readline().strip().split()
#     n = int(idiot[0])
#     d = int(idiot[1])
#     l = []
#     res = 0
#     # line = sys.stdin.readline().strip().split()
    # min_node = (int(line[0]), int(line[1]))
    # line = sys.stdin.readline().strip().split()
    # max_node = (int(line[0]), int(line[1]))
    # if max_node[1] < min_node[1]:
    #     max_node, min_node = min_node, max_node
    # if max_node[0] - min_node[0] >= d:
    #     res = max_node[1] + min_node[1]
    # for i in range(2, n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip().split()
    #     # 把每一行的数字分隔后转化成int列表
    #     # l.append((int(line[0]), int(line[1])))
    #     cor = int(line[0])
    #     money = int(line[1])
    #     if money > min_node[1]:
    #         if cor - max_node[0] >= d:
    #             res = money + max_node[1]
    #         elif cor - min_node[0] >= d:
    #
    #             inter = money + min_node[1]
    #             if inter > res:
    #                 res = inter
    #
    #         else:
    #             if money >= max_node[1]:
    #                 min_node = max_node
    #                 max_node = (cor, money)
    #             else:
    #                 min_node = (cor, money)

    # for i in range(1):
    #     for j in range(i+1, n):
    #         if l[j][0] - l[i][0] > d:
    #             inter = l[i][1]+l[j][1]
    #             if inter > res:
    #                 res = inter
    # print(res)


import sys
if __name__ == "__main__":
    # 读取第一行的n
    idiot = sys.stdin.readline().strip().split()
    n = int(idiot[0])
    d = int(idiot[1])
    l = []
    res = 0
    record = [-1] * n
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip().split()
        # 把每一行的数字分隔后转化成int列表
        l.append((int(line[0]), int(line[1])))
    # if
    # max_node = (l[1][0], l[1][1])
    max_node = (l[-1][0], l[-1][1])
    for i in range(1):
        for j in range(i+1, n):
            if l[j][0] - l[i][0] >= d:
                inter = l[i][1]+l[j][1]
                if inter > res:
                    res = inter
                    max_node = (l[j][0], l[j][1])
        record[i] = res
    for j in range(1,n-1):
        if l[j][1] < l[j-1][1]:
            # if max_node[0] - l[j][0] >
            continue
        else:
            t = 0
            for t in range(j-1, -1, -1):
                if record[t] > 0:
                    break
            node = l[t]
            for k in range(j + 1, n):
            # for k in range(j+1, max_node[0]):
                # if l[k][0] - node[0] >= d:
                #     break
                if l[k][0] - l[j][0] >= d and max_node[0] - l[j][0] >= d:
                    # if l[k][1] > max_node[1]:
                    inter = l[k][1] + l[j][1]
                    if inter > record[t]+l[j][1]-l[t][1]:

                        record[t] = inter
                        max_node = (l[k][0], l[k][1])
                    else:
                        record[t] = record[t]+l[j][1]-l[t][1]
                    break
                elif l[k][0] - l[j][0] >= d:
                    inter = l[k][1] + l[j][1]
                    if inter > record[j]:
                        record[j] = inter
                    max_node = (l[k][0], l[k][1])

                # else:
                #     inter = l[k][1] + l[j][1]
                #     if inter > res + l[j][1] - l[t][1]:
                #         res = inter
                #         max_node = (l[k][0], l[k][1])
                #     else:
                #         res = res + l[j][1] - l[t][1]
            # if max_inter_node[1] > max_node[1]
            # if res < max_node[1] + l[j][1]:
            #     res = max_node[1] + l[j][1]


    if l[-1][0] - l[-2][0] >= d and l[-1][1] + l[-2][1] > res:
        res = l[-1][1] + l[-2][1]
    print(res)