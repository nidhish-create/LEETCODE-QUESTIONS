class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]#reversing it first 
        carry =1#we will initialize carrey as 1 because what if we get [9,9,9]
        i=0#index @ 0
        while carry  :#carry =1
            if i <len(digits):#when i si inside the length if digits                           
                if digits[i]==9:#special case of carry 
                #then 9+1 = 0 1 will be the carry 
                    digits[i]=0  
                else:#when its not equal to  9 we will increment acc to question with one and we dont need carry at that time 
                                 
                    digits[i]+=1             
                    carry = 0
                
            else:#when i exceeds length of digits 
                digits.append(1)
                carry = 0
            i+=1#we have to increment our index evertime 
        return digits[::-1]#again reversing to get the correct order     
                
  
  
