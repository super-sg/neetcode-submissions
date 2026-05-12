class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,n in enumerate(nums):
            map[n]=i
        for i in range(len(nums)):
            n=target-nums[i]
            if n in map and map[n]!=i:
                return [i,map[n]]