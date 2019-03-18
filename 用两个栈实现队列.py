# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l = []
        self.l1 = []
    def push(self, node):
        # write code here
        # if self.l:
        #     self.l1.append(self.l.pop())
        self.l.append(node)
    def pop(self):
        # return xx
        if not self.l:
            return None
        while len(self.l) > 1:
            self.l1.append(self.l.pop())
        elem = self.l.pop()
        # self.l, self.l1 = self.l1, self.l
        while self.l1:
            self.l.append(self.l1.pop())
        return elem
