Time complexity O(n^2)
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result=[]
        for i in nums:
            count=0
            for j in range(len(nums)):
                if i>nums[j]:
                    count+=1
            result.append(count)
        return result


Time complexity O(n)
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        freq=[0]*101
        for num in nums:
            freq[num]+=1
        result=[]
        for num in nums:
            count=0
            for i in range(num):
                count+=freq[i]
            result.append(count)
        return result
        
