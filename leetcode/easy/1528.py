# 1528. Shuffle String

class Solution(object):
    def restoreString(self, s, indices):
        dic = {}
        for i in range(len(s)):
            dic[indices[i]] = s[i]
        sorted(dic.keys())
        return ''.join(dic[i] for i in range(len(dic)))

class Solution(object):
    def restoreString(self, s, indices):
        res = [''] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(i for i in res)