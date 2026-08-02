class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        maximum=0
        for num in nums:
            if num==1:
                count+=1
                if count>maximum:
                    maximum=count
            else:
                count=0
        return maximum
a=Solution()
print(a.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(a.findMaxConsecutiveOnes([1,0,1,1,0,1]))