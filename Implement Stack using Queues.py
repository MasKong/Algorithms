import queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.q = queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # self.q1 = queue.Queue()
        l = []
        while self.q.qsize() > 1:
            l.append(self.q.get())
        temp =  self.q.get()
        for i in l:
            self.q.put(i)
        return temp



    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        l = []
        while self.q.qsize():
            l.append(self.q.get())
        # temp = self.q.get()
        for i in l:
            self.q.put(i)
        return l[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.empty()

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(123)
param_2 = obj.pop()
obj.push(1)
obj.push(10)
obj.push(100)
param_3 = obj.top()
param_4 = obj.empty()

