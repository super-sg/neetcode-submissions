class Solution:
    def isnotalpha(self,i):
            if ord('a')<=ord(i.lower())<=ord('z') or 48<=ord(i.lower())<=57:
                return True
            return False
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.isnotalpha(s[l]):
                l+=1
            while r>l and not self.isnotalpha(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r=l+1,r-1
        return True