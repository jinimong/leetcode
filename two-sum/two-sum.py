class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {num: idx for idx, num in enumerate(nums)}
        
        for idx, num in enumerate(nums):
            idx2 = nums_dict.get(target - num)
            if idx2 is not None and idx != idx2:
                return [idx, idx2]
            
        return []
            