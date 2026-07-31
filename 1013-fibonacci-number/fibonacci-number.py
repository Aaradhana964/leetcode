class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)
a=Solution()
print(a.fib(2))
print(a.fib(3))
print(a.fib(4))