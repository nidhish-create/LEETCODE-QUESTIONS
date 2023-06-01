class Solution(object):
    def subsets(self, nums):
        
        ans =[[]]
            
        for i in nums:
            for j in range(len(ans)):
                ans.append(ans[j] + [i])
                      
        return ans
                
            
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
