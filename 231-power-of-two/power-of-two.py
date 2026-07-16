class Solution(object):
    def isPowerOfTwo(self, n):
        if n<0:
            return False
        x=0
        while pow(2,x)<=n:
            if n == pow(2,x):
                return True
            x+=1
        return False
a=Solution()
print(a.isPowerOfTwo(1))
print(a.isPowerOfTwo(16))
print(a.isPowerOfTwo(3))