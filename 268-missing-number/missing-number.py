class Solution(object):
    def missingNumber(self, nums):
       length=len(nums)
       total=length*(length+1)//2
       actual=sum(nums)
       return total-actual
a=Solution()
print(a.missingNumber([3,0,1]))
print(a.missingNumber([0,1]))
print(a.missingNumber([9,6,4,2,3,5,7,0,1]))    