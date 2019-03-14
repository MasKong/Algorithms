#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     l = [i for i in range(n, -1, -1)]
#     while l:
#         print("{}".format(l[0]), end=' ')
#         del l[0]
#         if l:
#             l.append(l[0])
#             l = l[1:]
#         else:
#             break
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     l = [i for i in range(n, 0, -1)]
#     # print(l)
#     while l:
#         elem = l.pop()
#         print("{}".format(elem), end=' ')
#         # del l[0]
#         if l:
#             elem = l.pop()
#             l.insert(0, elem)
#             # l = l[1:]
#         else:
#             break
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     l = [i for i in range(n, 0, -1)]
#     l1 = []
#     # print(l)
#     while len(l) > 1:
#         elem = l.pop()
#         print("{}".format(elem), end=' ')
#         # del l[0]
#         # if l:
#         elem = l.pop()
#         l.insert(0, elem)
#         #     # l = l[1:]
#         # else:
#         #     break
#     print(l[0])

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    l = [i for i in range(n, 0, -1)]
    def f(l):
        if not l:
            return
        l1 = []
        # print(l)
        while len(l)>1:
            elem = l.pop()
            print("{}".format(elem), end=' ')
            # del l[0]
            # if l:
            elem = l.pop()
            l1.append(elem)
            #     # l = l[1:]
            # else:
            #     break
        # l.insert()
        if l:
        #     print(l[0])
            l1.insert(0, l[0])
        l1 = l1[::-1]
        print(l1)
        f(l1)
    f(l)