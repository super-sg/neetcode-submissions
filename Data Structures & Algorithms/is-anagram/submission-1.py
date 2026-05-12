class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for i,j in zip(sorted(s),sorted(t)):
            if i==j:
                continue
            else:
                return False
        return True
            
            