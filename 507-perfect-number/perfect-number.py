class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
            if num<=1:
                return False
            totalsum=1
            i=2
            while i*i<num:
                if num%i==0:
                    totalsum+=i
                    totalsum+=num//i
                i+=1
            if i*i==num:
                totalsum+=i
            return totalsum==num