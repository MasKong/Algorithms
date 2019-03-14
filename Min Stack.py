class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x: int) -> None:
        self.l.append(x)
        # if not self.l:
        #     self.l.append(x)
        # elif x < self.top():
        #     self.l.append(x)
        # else:
        #     if len(self.l) == 1:
        #         self.l.insert(0, x)
        #     else:
        #         # for i in range(len(self.l)-2, -1, -1):
        #         i = len(self.l)-2
        #         while i > 0:
        #             if x < self.l[i]:
        #                 self.l.insert(i, x)
        #                 break
        #             i -= 1
        #         if i == 0:
        #             self.l.insert(i, x)


    def pop(self) -> None:
        if not self.l:
            raise ValueError
        elem = self.l[-1]
        self.l = self.l[:-1]
        return elem

    def top(self) -> int:
        if not self.l:
            raise ValueError
        return self.l[-1]

    def getMin(self) -> int:
        e_min = self.l[0]
        for i in self.l[1:]:
            if i < e_min:
                e_min = i
        return e_min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
# obj.push(0)
param_4 = obj.getMin()
# param_3 = obj.top()
obj.pop()
param_3 = obj.top()
param_2 = obj.getMin()
print(param_4)
print(param_3)
print(param_2)
# print(obj.top())
# param_4 = obj.getMin()
# obj.pop()
# param_4 = obj.getMin()
# obj.pop()
# param_4 = obj.getMin()
# obj.pop()
