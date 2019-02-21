class Solution:
    def addBinary_v1(self, a, b):
        # print(bin(int(a, 2) + int(b, 2)))
        return bin(int(a, 2) + int(b, 2))[2:]
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = []
        i, j = 0, 0
        flag = 0
        while i < len(a) and j < len(b):
            r = int(a[len(a)-i-1]) + int(b[len(b)-j-1]) + flag
            if r >= 2:
                if r == 2:
                    l.append(0)
                else:
                    l.append(1)
                flag = 1
            else:
                l.append(r)
                flag = 0
                # else:

            i += 1
            j += 1

        if i == len(a):
            while j < len(b):
                r = int(b[len(b)-j-1]) + flag
                if r == 2:
                    l.append(0)
                    # l.append(1)
                    flag = 1
                else:
                    l.append(r)
                    flag = 0
                j += 1


        else:
            while i < len(a):
                r = int(a[len(a)-i-1]) + flag
                if r == 2:
                    l.append(0)
                    # l.append(1)
                    flag = 1
                else:
                    l.append(r)
                    flag = 0
                i += 1
        if flag == 1:
            l.append(1)
        l.reverse()
        # print(l)
        return ''.join(str(e) for e in l)

s = Solution()
# print(s.addBinary('1010', '1011'))
print(s.addBinary_v1('11001', '101'))

