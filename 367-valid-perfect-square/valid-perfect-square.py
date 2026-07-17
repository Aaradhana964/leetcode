class Solution(object):
    def isPerfectSquare(self, num):
        i=0
        while i*i<=num:
            if i*i==num:
                return True
            i+=1
        return False
a=Solution()
print(a.isPerfectSquare(16))
print(a.isPerfectSquare(14))
