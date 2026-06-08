class Solution(object):
    def missingNumber(self, nums):
        actual_sum=0
        n=len(nums)
        expected_sum=n*(n+1)//2
        for i in nums:
            actual_sum += i
        return expected_sum-actual_sum
        
