class Solution(object):
    def firstUniqChar(self, s):
        import collections
        counter = collections.Counter(list(s))
        for i in range (len(s)):#we will iterate to check the unique element 
            if counter.get(s[i]) == 1:#if we have a unique eleemtn it will return its index i 
                return i 
        return -1                   
