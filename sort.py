class Sort():
    def __init__(self, l = None):
        if l is not None:
            assert type(l) == list,("please input a list")
        else:
            l = self._generate()
        self.l = l
        self.result = None


    def insert_sort(self):
        l = self.l      #add new reference to self.l, change l would change self.l
        for i in range(1,len(l)):   #use built-in methods to insert
            for j in range(i-1,-1,-1):
                if l[i] < l[j]:
                    if j == 0:
                        l.insert(j,l[i])
                        del(l[i+1])
                    elif l[i] >= l[j-1]:
                        l.insert(j, l[i])
                        del (l[i + 1])

    def insert_sort_v1(self):   #much slower than using built-in method
        l = self.l      #add new reference to self.l, change l would change self.l
        for i in range(1,len(l)):   #switch position
            for j in range(i-1,-1,-1):
                if l[j+1] < l[j]:
                    l[j], l[j+1] = l[j+1], l[j]


    def bubble_sort(self):
        l = self.l
        for i in range(0,len(l)-1):
            for j in range(0,len(l)-i-1):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]

    # def quick_sort(self):
    #     '''extra space usage'''
    #     '''divide the original into two parts such that elements in part a < that of part b'''
    #     l1 = []
    #     l2 = []
    #     pivot = self.l[-1]
    #     for i in self.l:
    #         if i <= pivot:
    #             l1.append(i)
    #         else:
    #             l2.append(i)
    #     l1.append(pivot)
    def quick_sort(self, p=None, r=None):
        '''extra space usage'''
        '''divide the original into two parts such that elements in part a < that of part b'''
        if p is None or r is None:
            p = 0
            r = len(self.l)
        # print("p ",p)
        # print("r ", r)
        if p<r-1:
            q = self._quick_sort_partition(p, r)
            # print("q ", q)
            self.quick_sort(p,q)
            self.quick_sort(q,r)
            # self._quick_sort_partition(p, q)
            # self._quick_sort_partition(q, r)
        # q = self._quick_sort_partition(p, r)
        # print(q)
        # while True:
        #     if self._quick_sort_partition(p, q) == 0:
        #         break
        # while True:
        #     if self._quick_sort_partition(q, r) == r-1:
        #         break
            # q = self._quick_sort_partition(0,len(self.l))
        # self.quick_sort(p,q)
        # self.quick_sort(q,r)
        # else:
        #     q = self._quick_sort_partition(p, r)
        #     self.quick_sort(p, q - 1)
        #     self.quick_sort(q, r)


    def _quick_sort_partition(self, p, r):
        # l = list(self.l)
        l = self.l
        i = p-1
        pivot = l[r-1]
        for j in range(p,r-1):      #in-place exchange without memory overhead
            if l[j] <= pivot:
                i += 1
                l[i], l[j] = l[j], l[i]
        # print(i)
        # print(l)
        l[i+1], l[r-1] = l[r-1], l[i+1]
        # print(l)
        # print(self.l)
        # print("i ",i)
        return i+1



    def merge_sort(self, p=None, r=None):
        l = self.l
        if p is None or r is None:
            p = 0
            r = len(l)      #not include r
        if p < r-1:
            q = int((p+r)/2)

            self.merge_sort(p,q)
            self.merge_sort(q, r)
            self.merge(p,q,r)


    def merge(self, p,q,r):
        l = self.l
        L = l[p:q]
        R = l[q:r]
        L.append(float('inf'))
        R.append(float('inf'))
        i,j = 0,0
        for k in range(p,r):    #r = len(list), not include r
            if L[i] < R[j]:
                l[k] = L[i]
                i+=1
            else:
                l[k] = R[j]
                j += 1


    def merge_two_lists(self,l1,l2):
        assert l1 is None or l2 is None,("empty list")
        l = []
        i = 0
        j = 0
        while i<len(l1) and j<len(l2):
            if l1[i] < l2[j]:
                l.append(l1[i])
                i+=1
            else:
                l.append(l2[j])
                j += 1
        if i == len(l1):
            l.extend(l2[j:])
        else:
            l.extend(l1[i:])
        return l



    def heap_sort(self):
        l = self.l
        self.heap_size = len(l)
        self.build_heap()
        for i in range(len(l)-1,0,-1):  #no need to include 0. change with itself is meaningless
            l[i], l[0] = l[0], l[i]
            self.heap_size -= 1
            self.max_heaplify(0)

    def build_heap(self):
        #bottom up. the first level of the tree has no child, no need to maintain
        for i in range(int(self.heap_size/2),-1,-1):
            self.max_heaplify(i)


    def max_heaplify(self,i):
        l = self.l
        left = 2*i +1
        right = 2*i +2
        largest = i
        if left < self.heap_size and l[left] > l[i]:
            largest = left

        if right < self.heap_size and l[right] > l[largest]:
            largest = right

        if largest != i:
            '''if position changes, need to recursively run max_heaplify to guarantee
            the descendant are also max heap'''
            l[i], l[largest] = l[largest], l[i]
            self.max_heaplify(largest)

    def _evaluate(self):
        if self.result is None:
            self.result = self.l
        for i in range(1,len(self.result)):
            if self.result[i] < self.result[i-1]:
                return False
        return True

    def _generate(self,length = None):
        try:
            import random
            if length is None:
                length = random.randint(0, 1000)
                # length = random.randint(0,100000)
            l = []
            for i in range(length):
                l.append(random.randint(-length,length))
            return l
        except ImportError:
            print("no random module, please input a sequence")

l = [4,6,1,0,5,-9,0,5,]
# l = [4,6,10,23,-1,-6]
# s = Sort(l)
# print(s._quick_sort_partition(0,len(l)))
# print(s.l)
s = Sort()
# s.quick_sort()
print("length ",len(s.l))
s.heap_sort()
# s.build_heap()
# s.merge_sort()
# s.insert_sort_v1()
# s.insert_sort()
print(s._evaluate())
# s._quick_sort_partition(0,len(l))
print(s.l)

def compare_time():
    import time
    print("**************compare time**************")
    s = Sort()
    l = s._generate(1000000)
    start_time = time.time()
    Sort(l).quick_sort()
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    Sort(l).merge_sort()
    print('--- {} seconds ---'.format(time.time() - start_time))
    start_time = time.time()
    Sort(l).heap_sort()
    print('--- {} seconds ---'.format(time.time() - start_time))

compare_time()