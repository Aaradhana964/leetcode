class Solution(object):
    def isAnagram(self, s, t):
        if sorted(s)==sorted(t):
            return True
        return False
a=Solution()
print(a.isAnagram("anagram","nagaram"))
print(a.isAnagram("rat","car"))