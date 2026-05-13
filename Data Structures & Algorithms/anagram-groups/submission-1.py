class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        l1 = set(tuple(sorted(i)) for i in strs)
        l=list(l1)
        l2=[]
        l3=[]
        for i in l:
            for j in strs:
                if tuple(sorted(j))==i:
                    l2.append(j)
            l3.append(l2)
            l2=[]
        return l3