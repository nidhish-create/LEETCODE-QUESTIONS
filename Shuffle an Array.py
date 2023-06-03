class Solution(object):

    def __init__(self, nums):
        
        self.nums = nums 
        """
        :type nums: List[int]  
        """                        
        

    def reset(self):
        return self.nums
        """
        :rtype: List[int]
        """
        

    def shuffle(self):
        arr = self.nums[:]
        n = len(arr)
        for i in range(n):
            rand = random.randint(i, n-1)
            arr[i], arr[rand] = arr[rand], arr[i]
        return arr 
    
        
        
        
        
        """
        :rtype: List[int]
        """
