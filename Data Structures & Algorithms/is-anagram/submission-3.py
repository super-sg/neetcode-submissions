class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        S={}
        T={}
        for i,j in zip(range(0,len(s)),range(0,len(t))):
            S[s[i]]=1+S.get(s[i],0)
            T[t[j]]=1+T.get(t[j],0)
        return S==T
            