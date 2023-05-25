from functools import cmp_to_key
class Solution:
   
    def compare(self,a,b):
        if int(str(a)+str(b)) > int(str(b)+str(a)):
            return -1
        if int(str(b)+str(a)) > int(str(a)+str(b)):
            return 1
        else:
            return 0
        
    def largestNumber(self, nums: List[int]) -> str:
        return str(int("".join([ str(i) for i in sorted(nums, key=functools.cmp_to_key(self.compare))]))) 
		
		
