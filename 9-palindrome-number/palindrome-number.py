class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        original=x
        def reverse(n,rev):
            if n==0:
                return rev
            return reverse(n//10,rev*10+n%10)
        return original==reverse(x,0)
a=Solution()
print(a.isPalindrome(121))
print(a.isPalindrome(-121)) 
print(a.isPalindrome(10))
