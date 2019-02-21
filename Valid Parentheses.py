class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l = []
        # record = l.pop()
        # while len(l) != 0:
        #     intermediate = l.pop()
        #     if
        # l.append(s[-1])
        for i in s[::-1]:
            if not l:   #if l is empty
                l.append(i)
            else:
                if self.valid_pattern(i,l[-1]):
                    l.pop()
                else:
                    l.append(i)
                    # return False
        if not l:
            return True
        return False

    def valid_pattern(self, a, b):
        if a == '(' and b == ')':
            return True
        if a == '{' and b == '}':
            return True
        if a == '[' and b == ']':
            return True

        return False

s = Solution()

a = "{[]}"
b = "()[]}"
leg = s.isValid(b)
print(leg)