class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for idx, num in enumerate(nums):
            value = target - num
            if value in d:
                return [d[value], idx]
            else:
                d[num] = idx
        
        return []
