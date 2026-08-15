class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper=0
        lower=0
        for ch in word:
            if 'A'<=ch<='Z':
                upper+=1
            else:
                lower+=1
        if upper==len(word):
            return True
        elif lower==len(word):
            return True
        elif 'A'<=word[0]<='Z'and lower==len(word)-1:
            return True
        else:
            return False