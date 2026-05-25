#O(n) time complexity space complexity 0(n)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        seen=set(nums)
        ans=[]
        for i in range(1,len(nums)+1):
            if i not in seen:
                ans.append(i)
        return ans

#optimal O(n) time complexity space complexity 0(1)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index= abs(nums[i])-1
            nums[index]=-abs(nums[index])
        ans=[]
        for i in range(len(nums)):
            if nums[i]> 0 :
                ans.append(i+1)
        return ans 
        
