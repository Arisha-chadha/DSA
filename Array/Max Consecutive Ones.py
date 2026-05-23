class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0 
        maxi=0
        for i in nums:
            if i == 1:
                count+=1
                maxi=max(count,maxi)
            else :
                count = 0 
        return maxi
        
