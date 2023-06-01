class Solution(object):
    def permute(self, nums):
        
        res = []
        
        #base case
        if (len(nums) == 1):#ssample input of nums = 1 then return it as a list or only  single permutation 
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)#first element i the list is popped while going thro the trree
            perms = self.permute(nums)#recursive call
            
            for perm in perms:
                perm.append(n)#the  n from which we jave popped is apoended like 2,3 3,2 it is appended and in the next step the poppped elemtn is extened with this to get the permutations
            res.extend(perms)
            nums.append(n)
        
        return res
