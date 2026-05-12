class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev=set()
        for i in nums:
            if i in prev:
                return True
            else:
                prev.add(i)
        return False