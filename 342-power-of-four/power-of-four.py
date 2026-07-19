class Solution(object):
    def isPowerOfFour(self, n):
        x=0
        while pow(4,x)<=n:
            if pow(4,x)==n:
                return True
            x+=1
        return False
a=Solution()
print(a.isPowerOfFour(16))
print(a.isPowerOfFour(5))
print(a.isPowerOfFour(1))