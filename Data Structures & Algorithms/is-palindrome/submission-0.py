class Solution:
    def isnotalpha(self,i):
            if ord('a')<=ord(i.lower())<=ord('z') or 48<=ord(i.lower())<=57:
                return True
            return False
    def isPalindrome(self, s: str) -> bool:
        st=''
        for i in s:
            if self.isnotalpha(i):
                st+=i.lower()
        l,r=0,len(st)-1
        while l<r:
            if st[l]==st[r]:
                l+=1
                r-=1
            else:
                return False
        return True

        