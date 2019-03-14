class Solution:
    def topKFrequent(self, words, k: int):
        d = {}
        for i in words:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        l = []
        for i in d.keys():
            l.append((i, d[i]))
        # l = list(map(lambda i: i[0], sorted(l, key=lambda i: i[1])[len(l) - k:]))
        # print(l)
        l = sorted(l, key=lambda i: i[1])
        # l = sorted(l, key=lambda i: i[1])[:k]

        l = l[::-1]
        # print(l)

        self.alpha_sort(l)
        print(l)

        return list(map(lambda i: i[0], l[:k]))

    def alpha_sort(self, l:list):
        for i in range(0, len(l)-1):
            j = i+1
            if l[j][1] != l[i][1]:
                continue
            while j < len(l):
                if l[j][0] < l[i][0] and l[j][1] == l[i][1]:
                    l[i], l[j] = l[j], l[i]
                elif l[j][1] != l[i][1]:
                    break
                j += 1








s = Solution()
# print(s.index_max_elem([2,4]))
res = s.topKFrequent(words=["glarko","zlfiwwb","nsfspyox","pwqvwmlgri","qggx","qrkgmliewc","zskaqzwo","zskaqzwo","ijy","htpvnmozay","jqrlad","ccjel","qrkgmliewc","qkjzgws","fqizrrnmif","jqrlad","nbuorw","qrkgmliewc","htpvnmozay","nftk","glarko","hdemkfr","axyak","hdemkfr","nsfspyox","nsfspyox","qrkgmliewc","nftk","nftk","ccjel","qrkgmliewc","ocgjsu","ijy","glarko","nbuorw","nsfspyox","qkjzgws","qkjzgws","fqizrrnmif","pwqvwmlgri","nftk","qrkgmliewc","jqrlad","nftk","zskaqzwo","glarko","nsfspyox","zlfiwwb","hwlvqgkdbo","htpvnmozay","nsfspyox","zskaqzwo","htpvnmozay","zskaqzwo","nbuorw","qkjzgws","zlfiwwb","pwqvwmlgri","zskaqzwo","qengse","glarko","qkjzgws","pwqvwmlgri","fqizrrnmif","nbuorw","nftk","ijy","hdemkfr","nftk","qkjzgws","jqrlad","nftk","ccjel","qggx","ijy","qengse","nftk","htpvnmozay","qengse","eonrg","qengse","fqizrrnmif","hwlvqgkdbo","qengse","qengse","qggx","qkjzgws","qggx","pwqvwmlgri","htpvnmozay","qrkgmliewc","qengse","fqizrrnmif","qkjzgws","qengse","nftk","htpvnmozay","qggx","zlfiwwb","bwp","ocgjsu","qrkgmliewc","ccjel","hdemkfr","nsfspyox","hdemkfr","qggx","zlfiwwb","nsfspyox","ijy","qkjzgws","fqizrrnmif","qkjzgws","qrkgmliewc","glarko","hdemkfr","pwqvwmlgri"]
, k=14)
print(res)
res = s.topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4)
print(res)
res = s.topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=1)
print(res)



