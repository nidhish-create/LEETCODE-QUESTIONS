class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""# we will first initialize the resuklt what if we dont have any common stings prefix so that we will returen the string as it is 
        for i in range(len(strs[0])):# then we will iterate through first chartacter of the string 
            for s in strs:#the we will check string 
                if i ==len(s) or s[i]!=strs[0][i]:#if a string in array the first charactewr is not equal to the  first character of the whole array of sring then no prefix is there 
                    return result 
            result +=strs[0][i]
        return result
