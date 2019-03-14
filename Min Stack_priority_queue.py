class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x: int) -> None:
        '''
        l includes tuples with the first element as the real element
        and the second element as the min element
        '''
        if not self.l:
            self.l.append((x, x))
        else:
            if x < self.l[-1][1]:
                self.l.append((x, x))
            else:
                self.l.append((x, self.l[-1][1]))


    def pop(self) -> None:
        if not self.l:
            raise ValueError
        elem = self.l[-1]
        self.l = self.l[:-1]
        return elem

    def top(self) -> int:
        if not self.l:
            raise ValueError
        return self.l[-1][0]

    def getMin(self) -> int:
        if not self.l:
            raise ValueError
        else:
            return self.l[-1][1]


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
