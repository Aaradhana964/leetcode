class Solution(object):
    def majorityElement(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for key, value in d.items():
            if value > len(nums) // 2:
                return key
        
a=Solution()
print(a.majorityElement([3,2,3]))
print(a.majorityElement([2,2,1,1,1,2,2]))