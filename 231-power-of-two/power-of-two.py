class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
a=Solution()
print(a.isPowerOfTwo(1))
print(a.isPowerOfTwo(16))
print(a.isPowerOfTwo(3))