class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            p=target-nums[i]
            if p in seen:
                return [seen[p],i]
            else:
                seen[nums[i]]=i
    