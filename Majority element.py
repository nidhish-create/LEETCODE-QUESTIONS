class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dict = {}
        for i in range(len(nums)):
            
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
                
        values = list(dict.values())
        keys = list(dict.keys())
        
        k = 0
          
        for i in range(len(values)):
            
            if values[i] > (len(nums)/2):
                k = keys[i]
        return k
