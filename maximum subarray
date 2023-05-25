class Solution(object):
    def maxSubArray(self, nums):
        
        maxSum =  nums[0]
        
        runningSum = 0
        
        for num in nums:
            runningSum += num
            if num > runningSum:
                runningSum = num
            maxSum = max(maxSum, runningSum)
        
        return maxSum
        """
        :type nums: List[int]
        :rtype: int
        """
